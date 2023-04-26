# CrOS IDE quickstart (go/cros-ide-quickstart)

CrOS IDE is a VSCode Extension for ChromiumOS development. It is a new project
and we currently support only internal developers at Google.

## Prerequisites

You need a ChromiumOS chroot. If you are a new member and don't have it, please
follow the [ChromiumOS Developer Guide] and set up your development environment,
so you can [enter the chroot via cros_sdk].

In this document, we assume ChromiumOS source code is in `~/chromiumos`.

[chromiumos developer guide]: https://chromium.googlesource.com/chromiumos/docs/+/HEAD/developer_guide.md
[enter the chroot via cros_sdk]: https://chromium.googlesource.com/chromiumos/docs/+/HEAD/developer_guide.md#Enter-the-chroot

## 1. Install Visual Studio Code

First, you need to install Visual Studio Code (VSCode) on your client machine.

### gLinux

Check if it's already installed by running `code` in terminal or look for it in
the application menu, otherwise:

```shell
(outside) $ (cd &&
    sudo glinux-add-repo typescript stable &&
    sudo apt update &&
    sudo apt install code)
```

Learn more at [go/vscode/install#glinux]

[go/vscode/install#glinux]: http://go/vscode/install#glinux

### gMac

Install [VSCode from the Software Center] or
[go/mule](`sudo mule install visual-studio-code`).

[vscode from the software center]: http://go/softwarecenter/list//appid%3AMAC_OS-visual-studio-code/MAC_OS
[go/mule]: http://go/mule

### ChromeOS

CrOS IDE supports only platform-specific VSCode, which is not available for
ChromeOS. There are two workarounds:

-   Check out [go/cros-ide-on-chromebooks] to learn more about [Code Server],
    which is a Web IDE accessible in the browser.
-   Use Chrome Remote Desktop.

[go/cros-ide-on-chromebooks]: http://go/cros-ide-on-chromebooks
[code server]: https://github.com/coder/code-server

## 2. (Optional) Connect to your machine via VSCode

If you use remote setup, for example gMac laptop, you will need
[Remote development] extension.

Install [Remote development] extension on the VSCode. Click the lower left "Open
a Remote Window" button and select \[Connect to Host...\] command (alternatively
directly choose this command from the command palette), select your remote
machine, and open your working directory under `~/chromiumos/`.

[remote development]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

## 3. Install the extension

Open *View &rarr; Extensions* in VSCode (Ctrl+Shift+X), search [CrOS IDE] and
install it.

[cros ide]: https://marketplace.visualstudio.com/items?itemName=Google.cros-ide

## 4. Open a folder

Finally, open a folder with sources to let CrOS IDE detect the chroot. Select
*File &rarr; Open Folder...*, choose, for example, `~/chromiumos/src/platform2`,
and you are good to go.

# Using CrOS IDE

Check out **[go/cros-ide-features]** to learn more about features, known issues,
and useful tips.

## Selected Features

See [go/cros-ide-features] for all the features.

[go/cros-ide-features]: http://go/cros-ide-features

### [Code Completion and Navigation]

Code completion in C++ is available in platform2 packages which support
`USE=compdb_only`. Press F12 to [Go to Definition], Ctrl+F12 to Go to
Implementation, and so on.

[go to definition]: https://code.visualstudio.com/docs/editor/editingevolved#_go-to-definition
[Code Completion and Navigation]: http://go/cros-ide-doc-platform2-cpp

### [Device Management]

CrOS IDE provides a view to manage your test devices. With the built-in VNC
client, you can control a device remotely.

[Device Management]: http://go/cros-ide-doc-device-management

### [Linter Integration]

CrOS IDE exposes lint errors found by `cros lint` and similar tools in C++,
Python, shell, and GN files. We run linters every time a file is saved, and mark
errors with squiggly lines in the editor and show them in the *Problems* box and
on mouse hover. This feature brings to your attention errors which block `repo
upload`.

[Linter Integration]: http://go/cros-ide-doc-linting

### [Boards and Packages]

CrOS IDE shows which packages you are working on and lets you run `cros_workon
start/stop` directly from the UI. Access it by clicking on *CrOS Development*
[activity bar] (Chrome icon). Use +/– buttons to start and stop working on packages.

[activity bar]: https://code.visualstudio.com/docs/getstarted/userinterface
[Boards and Packages]: http://go/cros-ide-doc-boards-pkgs

### [Code Search]

You can easily open the current file in Code Search from the context menu in a
text editor. Go to [settings] to choose whether to chose which instance to use
(public, internal, or Gitiles).

[settings]: https://code.visualstudio.com/docs/getstarted/settings
[Code Search]: http://go/cros-ide-doc-code-search

### Filing bugs

If you find issues or have feature requests, feel free to file bugs at
[go/cros-ide-new-bug]. You can also do it by clicking the [feedback button].

[go/cros-ide-new-bug]: http://go/cros-ide-new-bug
[feedback button]: http://go/cros-ide-doc-feedback-button
