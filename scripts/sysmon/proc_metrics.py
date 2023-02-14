# Copyright 2017 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Process metrics."""

from __future__ import absolute_import

from functools import partial
import logging

import psutil  # pylint: disable=import-error

from chromite.lib import metrics


logger = logging.getLogger(__name__)

_count_metric = metrics.GaugeMetric(
    "proc/count", description="Number of processes currently running."
)
_thread_count_metric = metrics.GaugeMetric(
    "proc/thread_count", description="Number of threads currently running."
)
_cpu_percent_metric = metrics.GaugeMetric(
    "proc/cpu_percent", description="CPU usage percent of processes."
)
_cpu_times_metric = metrics.CumulativeMetric(
    "proc/cpu_times",
    description="Accumulated CPU time in each specific mode of processes.",
)


def collect_proc_info():
    collector = _ProcessMetricsCollector()
    collector.collect()


class _ProcessMetricsCollector(object):
    """Class for collecting process metrics."""

    # We need to store some per process metrics of last run in order to
    # calculate the detla and aggregate them.
    old_cpu_times = {}

    def __init__(self):
        self._metrics = [
            _ProcessMetric("adb", test_func=partial(_is_process_name, "adb")),
            _ProcessMetric("autoserv", test_func=_is_parent_autoserv),
            _ProcessMetric(
                "bbagent", test_func=partial(_is_process_name, "bbagent")
            ),
            _ProcessMetric(
                "cache-downloader",
                test_func=partial(_is_process_name, "downloader"),
            ),
            _ProcessMetric("cipd", test_func=partial(_is_process_name, "cipd")),
            _ProcessMetric(
                "cloudtail", test_func=partial(_is_process_name, "cloudtail")
            ),
            _ProcessMetric(
                "common-tls", test_func=partial(_is_process_name, "common-tls")
            ),
            _ProcessMetric("curl", test_func=partial(_is_process_name, "curl")),
            _ProcessMetric(
                "dnsmasq", test_func=partial(_is_process_name, "dnsmasq")
            ),
            _ProcessMetric(
                "drone-agent",
                test_func=partial(_is_process_name, "drone-agent"),
            ),
            _ProcessMetric(
                "fleet-tlw", test_func=partial(_is_process_name, "fleet-tlw")
            ),
            _ProcessMetric(
                "getty", test_func=partial(_is_process_name, "getty")
            ),
            _ProcessMetric(
                "gs_offloader",
                test_func=partial(_is_process_name, "gs_offloader.py"),
            ),
            _ProcessMetric("gsutil", test_func=_is_gsutil),
            _ProcessMetric("java", test_func=partial(_is_process_name, "java")),
            _ProcessMetric("k8s_system", test_func=_is_k8s_system),
            _ProcessMetric(
                "labservice", test_func=partial(_is_process_name, "labservice")
            ),
            _ProcessMetric(
                "lxc-attach", test_func=partial(_is_process_name, "lxc-attach")
            ),
            _ProcessMetric(
                "lxc-start", test_func=partial(_is_process_name, "lxc-start")
            ),
            _ProcessMetric(
                "podman-pull", test_func=partial(_is_podman, "pull")
            ),
            _ProcessMetric("podman-run", test_func=partial(_is_podman, "run")),
            _ProcessMetric(
                "phosphorus", test_func=partial(_is_process_name, "phosphorus")
            ),
            _ProcessMetric("recipe", test_func=_is_recipe),
            _ProcessMetric("sshd", test_func=partial(_is_process_name, "sshd")),
            _ProcessMetric("swarming_bot", test_func=_is_swarming_bot),
            _ProcessMetric(
                "swarming_sub_task", test_func=_is_swarming_sub_task
            ),
            _ProcessMetric(
                "sysmon",
                test_func=partial(_is_python_module, "chromite.scripts.sysmon"),
            ),
            _ProcessMetric("tko_proxy", test_func=_is_tko_proxy),
        ]
        self._other_metric = _ProcessMetric("other")

    def collect(self):
        new_cpu_times = {}
        for proc in psutil.process_iter():
            new_cpu_times[proc.pid] = proc.cpu_times()
            self._collect_proc(proc)
        self._flush()
        _ProcessMetricsCollector.old_cpu_times = new_cpu_times

    def _collect_proc(self, proc):
        for metric in self._metrics:
            if metric.add(proc):
                break
        else:
            self._other_metric.add(proc)

    def _flush(self):
        for metric in self._metrics:
            metric.flush()
        self._other_metric.flush()


class _ProcessMetric(object):
    """Class for gathering process metrics."""

    def __init__(self, process_name, test_func=lambda proc: True):
        """Initialize instance.

        process_name is used to identify the metric stream.

        test_func is a function called
        for each process.  If it returns True, the process is counted.  The
        default test is to count every process.
        """
        self._fields = {
            "process_name": process_name,
        }
        self._test_func = test_func
        self._count = 0
        self._thread_count = 0
        self._cpu_percent = 0
        self._cpu_times = _CPUTimes()

    def add(self, proc):
        """Do metric collection for the given process.

        Returns True if the process was collected.
        """
        if not self._test_func(proc):
            return False
        self._count += 1
        self._thread_count += proc.num_threads()
        self._cpu_percent += proc.cpu_percent()

        self._cpu_times += _CPUTimes(
            proc.cpu_times()
        ) - _ProcessMetricsCollector.old_cpu_times.get(proc.pid)

        return True

    def flush(self):
        """Finish collection and send metrics."""
        _count_metric.set(self._count, fields=self._fields)
        self._count = 0

        _thread_count_metric.set(self._thread_count, fields=self._fields)
        self._thread_count = 0

        _cpu_percent_metric.set(
            int(round(self._cpu_percent)), fields=self._fields
        )
        self._cpu_percent = 0

        for mode, t in self._cpu_times.asdict().items():
            _cpu_times_metric.increment_by(
                t, fields={**self._fields, "mode": mode}
            )
        self._cpu_times = _CPUTimes()


class _CPUTimes(object):
    """A container for CPU times metrics."""

    def __init__(self, v=None):
        self.system = v.system if v else 0
        self.user = v.user if v else 0
        self.iowait = v.iowait if v else 0
        self.children_system = v.children_system if v else 0
        self.children_user = v.children_user if v else 0

    def __sub__(self, rhs):
        if not rhs:
            return self

        r = _CPUTimes()
        r.system = self.system - rhs.system
        r.user = self.user - rhs.user
        r.iowait = self.iowait - rhs.iowait
        r.children_system = self.children_system - rhs.children_system
        r.children_user = self.children_user - rhs.children_user
        return r

    def __iadd__(self, rhs):
        if not rhs:
            return self

        self.system += rhs.system
        self.user += rhs.user
        self.iowait += rhs.iowait
        self.children_system += rhs.children_system
        self.children_user += rhs.children_user
        return self

    def asdict(self):
        return {
            "system": self.system,
            "user": self.user,
            "iowait": self.iowait,
            "children_system": self.children_system,
            "children_user": self.children_user,
        }


def _is_parent_autoserv(proc):
    """Return whether proc is a parent (not forked) autoserv process."""
    return _is_autoserv(proc) and not _is_autoserv(proc.parent())


def _is_autoserv(proc):
    """Return whether proc is an autoserv process."""
    # This relies on the autoserv script being run directly.  The script should
    # be named autoserv exactly and start with a shebang that is /usr/bin/python,
    # NOT /bin/env
    return _is_process_name("autoserv", proc)


def _is_python_module(module, proc):
    """Return whether proc is a process running a Python module."""
    cmdline = proc.cmdline()
    return (
        cmdline
        and cmdline[0].endswith("python")
        and cmdline[1:3] == ["-m", module]
    )


def _is_process_name(name, proc):
    """Return whether process proc is named name."""
    return proc.name() == name


def _is_recipe(proc):
    """Return whether proc is a recipe process.

    An example proc is like
    '/home/.../bin/python -u -s
        /home/.../kitchen-checkout/recipe_engine/recipe_engine/main.py ...'.
    """
    cmdline = proc.cmdline()
    return (
        len(cmdline) >= 4
        and cmdline[0].endswith("/python")
        and cmdline[3].endswith("/recipe_engine/main.py")
    )


def _is_swarming_bot(proc):
    """Return whether proc is a Swarming bot.

    A swarming bot process is like '/usr/bin/python3.8 <bot-zip-path> start_bot'.
    """
    cmdline = proc.cmdline()
    return (
        len(cmdline) == 3
        and cmdline[0].split("/")[-1].startswith("python")
        and cmdline[2] == "start_bot"
    )


def _is_swarming_sub_task(proc):
    """Return whether proc is a Swarming bot sub task.

    An example Swarming sub task:
        /usr/bin/python3.8 -u /.../swarming_bot.2.zip run_isolated ...
    """
    cmdline = proc.cmdline()
    return (
        len(cmdline) >= 4
        and cmdline[0].split("/")[-1].startswith("python")
        and cmdline[2].split("/")[-1].startswith("swarming_bot.")
    )


def _is_gsutil(proc):
    """Return whether proc is gsutil."""
    cmdline = proc.cmdline()
    return (
        len(cmdline) >= 2
        and cmdline[0] == "python"
        and cmdline[1].endswith("gsutil")
    )


def _is_k8s_system(proc):
    """Return whether proc is a k8s system process."""
    return proc.name() in ("kubelet", "kube-proxy")


def _is_tko_proxy(proc):
    """Return whether proc is a tko proxy.

    A tk proxy process is like
    '/opt/cloud_sql_proxy -dir=<...>
        -instances=google.com:chromeos-lab:us-central1:tko
        -credential_file=<...>'.
    """
    cmdline = proc.cmdline()
    return (
        len(cmdline) == 4
        and cmdline[0].split("/")[-1] == "cloud_sql_proxy"
        and cmdline[2] == "-instances=google.com:chromeos-lab:us-central1:tko"
    )


def _is_podman(subcmd, proc):
    """Return whiter proc is a podman process.

    A podman pull process is like
    'podman pull image:tag'
    A podman run process is like
    'podman run --option ... image:tag'
    """
    cmdline = proc.cmdline()
    return proc.name() == "podman" and len(cmdline) > 1 and cmdline[1] == subcmd
