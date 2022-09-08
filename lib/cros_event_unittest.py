# Copyright 2016 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unit tests for chros_event"""

import io
import json

from chromite.lib import cros_event
from chromite.lib import cros_test_lib


class EventIdGeneratorTest(cros_test_lib.TestCase):
    """Test EventIdGenerator fuction"""

    def testEventIdGenerator(self):
        expected_ids = {1, 2, 3, 4, 5}
        id_gen = cros_event.EventIdGenerator()
        for expected_id in expected_ids:
            self.assertEqual(expected_id, next(id_gen))


class FailTest(cros_test_lib.TestCase):
    """Test Failure class"""

    def testInit(self):
        f1 = cros_event.Failure()
        self.assertIsInstance(f1, Exception)
        self.assertEqual(f1.status, cros_event.EVENT_STATUS_FAIL)

        f2_msg = "This is the message for the failure"
        f2 = cros_event.Failure(f2_msg)
        self.assertEqual(f2.status, cros_event.EVENT_STATUS_FAIL)
        self.assertEqual(f2.msg, f2_msg)


class EventTest(cros_test_lib.TestCase):
    """Test Event class"""

    # pylint: disable=attribute-defined-outside-init
    def setUp(self):
        self._resetEmit()

        self.id1 = 1
        self.data1 = {1: "a", 2: "b", 3: "c"}
        self.event1 = cros_event.Event(
            eid=self.id1, data=self.data1, emit_func=self.emitHook
        )

    def emitHook(self, event):
        self.emitCalled = True
        self.emitEvent = event

    def _resetEmit(self):
        self.emitCalled = False
        self.emitEvent = None

    def testInit(self):
        self.assertEqual(self.event1[cros_event.EVENT_ID], self.id1)
        # pylint: disable=dict-items-not-iterating
        self.assertGreaterEqual(self.event1.items(), self.data1.items())

        self.assertIsInstance(self.event1, dict)

    def testWithSuccess(self):
        """test success case"""
        with self.event1 as e:
            self.assertEqual(self.event1, e)
            self.assertEqual(
                e[cros_event.EVENT_STATUS], cros_event.EVENT_STATUS_RUNNING
            )

        self.assertTrue(self.emitCalled)
        self.assertEqual(
            self.emitEvent[cros_event.EVENT_STATUS],
            cros_event.EVENT_STATUS_PASS,
        )

    def testWithFailureCall(self):
        """test with fail() call"""
        failMsg = "failed, as it should correctly"

        with self.event1 as e:
            e.fail(message=failMsg)

        self.assertEqual(
            self.emitEvent[cros_event.EVENT_STATUS],
            cros_event.EVENT_STATUS_FAIL,
        )
        self.assertEqual(self.emitEvent[cros_event.EVENT_FAIL_MSG], failMsg)

    def testWithFailureCallWithStatus(self):
        """test with fail() and custom status call"""
        failMsg = "failed, as it should correctly"
        customStatus = "UnitTestFailure"

        with self.event1 as e:
            e.fail(message=failMsg, status=customStatus)

        self.assertEqual(self.emitEvent[cros_event.EVENT_STATUS], customStatus)
        self.assertEqual(self.emitEvent[cros_event.EVENT_FAIL_MSG], failMsg)

    def testWithFailure(self):
        """test with raising failure exception"""
        failMsg = "failed, as it should correctly"

        with self.event1:
            raise cros_event.Failure(failMsg)

        self.assertEqual(
            self.emitEvent[cros_event.EVENT_STATUS],
            cros_event.EVENT_STATUS_FAIL,
        )
        self.assertEqual(self.emitEvent[cros_event.EVENT_FAIL_MSG], failMsg)

    def testWithExceptionFail(self):
        """test with raised non-Failure exception"""
        try:
            with self.event1:
                raise NameError
        except NameError:
            self.assertEqual(
                self.emitEvent[cros_event.EVENT_STATUS],
                cros_event.EVENT_STATUS_FAIL,
            )


class EventLoggerTest(cros_test_lib.TestCase):
    """Test EventLogger class"""

    # pylint: disable=attribute-defined-outside-init

    def emitHook(self, event):
        self.emitCalled = True
        self.emitEvent = event

    def _resetEmit(self):
        self.emitCalled = False
        self.emitEvent = None

    def setUp(self):
        self._resetEmit()

        self.data1 = {1: 2, 3: 4}

        self.events = []
        self.log1 = cros_event.EventLogger(self.emitHook, data=self.data1)

    def testEvent(self):
        e_data = {"one": "two", "three": "four"}

        e = self.log1.Event(data=e_data)

        # pylint: disable=dict-items-not-iterating
        self.assertGreaterEqual(e.items(), e_data.items())
        self.assertGreaterEqual(e.items(), self.data1.items())

    def testEventWithKind(self):
        kind = "testStep"
        e = self.log1.Event(kind=kind)
        self.assertEqual(e["id"][0], kind)


class EventFileLoggerTest(cros_test_lib.TestCase):
    """Test EventFileLogger class"""

    # pylint: disable=attribute-defined-outside-init

    def encode_func(self, event):
        self.emitEvent = event
        return json.dumps(event)

    def get_event_from_file(self):
        event_str = self.file_out.getvalue()
        self.file_out.buf = ""  # Clear out StringIO buffer
        return json.loads(event_str)

    def setUp(self):
        self.data1 = {"one": 2, "two": 4}
        self.emitEvent = None
        self.file_out = io.StringIO()
        self.log = cros_event.EventFileLogger(
            self.file_out, data=self.data1, encoder_func=self.encode_func
        )

    def testInit(self):
        self.assertIsInstance(self.log, cros_event.EventLogger)

    def testEvents(self):
        with self.log.Event():
            pass

        self.assertDictEqual(self.emitEvent, self.get_event_from_file())

    def testEventFail(self):
        with self.log.Event():
            raise cros_event.Failure("always fail")

        self.assertDictEqual(self.emitEvent, self.get_event_from_file())

    def testShutdown(self):
        self.log.shutdown()


class EventStubLogger(cros_test_lib.TestCase):
    """Test EventStubLogger class"""

    def setUp(self):
        self.log = cros_event.EventStubLogger()

    def testInit(self):
        self.assertIsInstance(self.log, cros_event.EventLogger)


class FunctionTest(cros_test_lib.TestCase):
    """Test Module Tests"""

    def setUp(self):
        self._last_root = cros_event.root

    def tearDown(self):
        if hasattr(self, "_last_root") and self._last_root:
            cros_event.setEventLogger(self._last_root)

    def SetEventLoggerTest(self):
        new_log = cros_event.EventStubLogger()
        cros_event.setEventLogger(new_log)
        self.assertEqual(new_log, cros_event.root)

    def newEventTest(self):
        e1 = cros_event.newEvent()
        self.assertIsInstance(e1, cros_event.Event)

        e2 = cros_event.newEvent(foo="bar")
        self.assertIsInstance(e2, cros_event.Event)
        self.assertEqual("bar", e2["foo"])

        test_kind = "testKind"
        e3 = cros_event.NewEvent(kind=test_kind)
        self.assertEqual(e3["id"][0], test_kind)
