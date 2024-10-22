#!/bin/bash
<<EOF

   Blog Tool \ Setup \ Tooling \ Poetry

   Setup the tooling for Poetry, so that project dependencies and environment can be installed

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared_functions.sh"
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
