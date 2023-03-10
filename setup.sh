#!/bin/bash
<<EOF

   Blog Tool \ Python \ Setup

   A simple shell script for setting up and configuring the local development environment for macOS and Linux (Debian).

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/../../shell/shared)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared.sh"
write_header

usage() {
    write_info "setup" "usage - setup"
    write_info "setup" "./setup.sh [-t <target path>] [-h]"
    exit 1
}

if ! is_python_available; then
    write_error "setup" "python is not available from the command-line, or installed."
    exit 3
fi

while getopts ':t:h?' opt; do
    case $opt in
    t)
        TARGET_PATH=$OPTARG
        write_warning "setup" "target path for project is \"$OPTARG\""
        ;;
    h | ?)
        usage
        ;;
    :)
        write_error "setup" "\"-${OPTARG}\" requires an argument."
        usage
        ;;
    *)
        write_error "setup" "\"-${OPTARG}\" is not recognised."
        usage
        ;;
    esac
done

if [ -z $TARGET_PATH ]; then
    write_warning "setup" "target path for the virtual environment not defined. using \"$CURRENT_SCRIPT_DIRECTORY/venv\""
    TARGET_PATH=$CURRENT_SCRIPT_DIRECTORY/venv
fi

if ! is_virtualenv_available; then
    write_warning "setup" "no virtual environment was found. creating."
    if ! create_virtualenv $TARGET_PATH; then
        write_error "setup" "failed to create the virtualenv"
    else
        write_success "setup" "successfully created virtual environment"
    fi
fi

write_info "setup" "installing dependencies"

pip install -r requirements.txt


write_success "setup" "done"