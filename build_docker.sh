#!/bin/bash
<<EOF

   Blog Tool \ Build \ Docker

   Build the Docker container image for this tool, so it can be launched or invoked as a Docker container.

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

ALLOWED_CONFIGURATIONS=(development production)

usage() {
    write_info "build-docker" "./build-docker.sh"
    exit 1
}

while getopts ':c:h?' opt; do
   case $opt in
        c)
            TARGET_CONFIGURATION=${OPTARG}
            ;;
        h|?)
            usage
            ;;
        :)
            write_error "build-docker" "\"-${OPTARG}\" requires an argument"
            usage
            ;;
        *)
            write_error "build-docker" "\"-${OPTARG}\"was not recognised as an option"
            usage
            ;;
   esac
done

write_success "build-docker" "done"
exit 0