#!/bin/bash
<<EOF

   Blog Tool \ Generate \ Documentation

   Generate documentation for the project

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared-functions.sh"
write_header

write_success "generate-docs" "done"
exit 0