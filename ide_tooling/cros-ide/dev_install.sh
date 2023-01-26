#!/bin/bash
# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

USAGE="Usage:
 dev_install.sh [options]

Options:
 --exe path|name
    Specify the VS Code executable. By default 'code' is used. You need to set
    this flag if you are using code-server or code-insiders

 --help
    Print this message
"

set -e

terminal_color_clear='\033[0m'
terminal_color_warning='\033[1;31m'
min_node_ver=v14

echoWarning() {
  printf "${terminal_color_warning}%s${terminal_color_clear}\n" "$1"
}

cd "$(dirname "$0")"

if ! which node > /dev/null; then
  echoWarning "node not found; please install it following \
http://go/nodejs/installing-node"
  exit 1
fi

current_version="$(node --version)";
if [[ "${current_version}" < "${min_node_ver}" ]]; then
  echoWarning "Node version ${current_version} is too low. Please get node \
${min_node_ver} or higher to avoid unexpected issues."
  exit 1
fi

exe="code"

while [ $# -gt 0 ]; do
  if [[ "$1" == '--exe' ]]; then
    exe="$2"
    shift
  fi
  if [[ "$1" == '--help' ]]; then
    echo "${USAGE}"
    exit 0
  fi
  shift
done

if ! which "${exe}" > /dev/null; then
  echo "VSCode executable not found. Did you forget --exe ?"
  exit 1
fi

npm ci

previous_version="$(npm pkg get version)"
# Trim leading and trailing double quotes.
previous_version="${previous_version%\"}"
previous_version="${previous_version#\"}"

npm version prerelease --preid=dev

td="$(mktemp -d)"

npx vsce package -o "${td}/"

"${exe}" --force --install-extension "${td}"/*

rm -r "${td}"

npm version "${previous_version}"
