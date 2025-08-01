#!/bin/bash

## Copyright (C) 2024 - 2025 ENCRYPTED SUPPORT LLC <adrelanos@whonix.org>
## See the file COPYING for copying conditions.

set -x
set -e
set -o nounset
set -o errtrace
set -o pipefail

dpkg -l | grep pyqt5-dev-tools
true "INFO: package qtchooser contains 'designer' program"

mode="${1:-build}"
project_name="sysmaint_panel"

project_base_dir="$(dirname -- "$(readlink -f -- "${0}")")";

if [ "${mode}" = 'build' ]; then
  for ui_file in "${project_base_dir}"/ui/*; do
    ui_file_basename="$(basename -- "${ui_file}")"
    ui_py_file_basename="$(cut -d'.' -f1 <<< "${ui_file_basename}")_ui.py"
    pyuic5 "${ui_file}" | tee -- "${project_base_dir}/usr/lib/python3/dist-packages/${project_name}/${ui_py_file_basename}" > /dev/null
    sed -i '/^#/d' "${project_base_dir}/usr/lib/python3/dist-packages/${project_name}/${ui_py_file_basename}"
  done
elif [ "${mode}" = 'clean' ]; then
  for ui_file in "${project_base_dir}/usr/lib/python3/dist-packages/${project_name}"/*_ui.py; do
    if [ -f "${ui_file}" ]; then
      printf '%s\n' "Removing file '${ui_file}'"
      safe-rm -- "${ui_file}"
    fi
  done
else
  printf '%s\n' "ERROR: Unrecognized mode '${mode}'!"
  exit 1
fi
