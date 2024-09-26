#!/usr/bin/env bash
function _test_file_path_exist_or_exit()
{
  local FILE_PATH_TO_TEST

  FILE_PATH_TO_TEST="${1}"

  if [[ ! -f "${FILE_PATH_TO_TEST}" ]];
  then
    echo ":: ERROR"
    echo "   Mandatory file does not exist >>${FILE_PATH_TO_TEST}<<."

    exit 10
  fi
}

function _main()
{
  local ENVIRONMENT_FILE_PATH
  local FILE_BASE_PATH
  local PROJECT_BASE_PATH

  FILE_BASE_PATH=$(realpath $(dirname ${0}))

  PROJECT_BASE_PATH=$(realpath ${FILE_BASE_PATH}/..)

  ENVIRONMENT_FILE_PATH="${PROJECT_BASE_PATH}/.env"
  PYTHON_PROGRAMM_FILE_PATH="${PROJECT_BASE_PATH}/cli.py"
  PYTHON_VENV_FILE_PATH="${PROJECT_BASE_PATH}/.venv/bin/activate"

  _test_file_path_exist_or_exit "${ENVIRONMENT_FILE_PATH}"
  _test_file_path_exist_or_exit "${PYTHON_PROGRAMM_FILE_PATH}"
  _test_file_path_exist_or_exit "${PYTHON_VENV_FILE_PATH}"

  source "${PYTHON_VENV_FILE_PATH}"

  # ref: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
  set -a
  source "${ENVIRONMENT_FILE_PATH}"
  set +a

  python "${PYTHON_PROGRAMM_FILE_PATH}" "${@}"
}

_main "${@}"
