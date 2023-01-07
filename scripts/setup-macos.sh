#!/bin/bash
<<EOF

   Blog Tool \ Setup \ MacOS

   Perform setup operations for macOS

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared-functions.sh"
write_header

write_info "setup-macos" "installing dependencies for macos"
brew install openssl readline sqlite3 xz zlib tcl-tk
if ! write_response "setup-macos" "install: dependencies"; then
    write_error "setup-macos" "failed: unable to install dependencies for macos"
    exit 1
fi

write_success "setup-macos" "done"
exit 0