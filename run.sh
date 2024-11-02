#!/usr/bin/env bash
<<EOF

   Blog Tool \ Scripts \ Run

   Run all scripts that are in the base of the project.

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV/scripts)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

for scriptfile in $CURRENT_SCRIPT_DIRECTORY_ENV/run_*.sh; do
    write_info "run" "Running $(basename $scriptfile)"
    "$scriptfile"
done

write_success "run" "Done"
exit 0