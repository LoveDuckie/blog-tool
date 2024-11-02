#!/bin/bash
<<EOF

   Blog Tool \ Setup \ Tooling \ Poetry

   Setup the tooling for Poetry, so that project dependencies and environment can be installed

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

export DEBIAN_FRONTEND=noninteractive
write_info "setup-debian" "updating: apt packages"
apt -yqq update && apt -yqq upgrade

write_info "setup-debian" "installing: apt packages"
apt -yqq install curl git build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

write_success "setup-debian" "done"
exit 0
