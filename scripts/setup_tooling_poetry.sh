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

if is_command_available poetry; then
    write_warning "setup-tooling-poetry" "poetry is already installed on this system"
    exit 0
fi

write_info "setup-tooling-poetry" "installing poetry"
curl -sSL https://install.python-poetry.org | python3 -
if ! write_response "setup-tooling-poetry" "install: poetry"; then
    write_error "setup-tooling-poetry" "failed: installing poetry"
    exit 2
fi

echo "export PATH=\"~/.local/bin:\$PATH\"" >>~/.profile
. ~/.profile

if ! is_command_available poetry; then
    write_error "setup-tooling-poetry" "poetry was not installed correctly"
    exit 3
fi

write_success "setup-tooling-poetry" "done"
exit 0
