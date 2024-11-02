#!/bin/bash
<<EOF

   Blog Tool \ Scripts \ Run Lint

   Run linting operations using pylint with a pylintrc configuration, within a virtual environment

EOF

CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV/scripts)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

# Check if virtualenv is installed, install if not
if ! command -v virtualenv &> /dev/null
then
    write_warning "run_lint" "virtualenv is not installed. Installing..."
    pip install virtualenv
fi

# Create a virtual environment if it doesn't already exist
VENV_DIR="$CURRENT_SCRIPT_DIRECTORY_ENV/venv"
if [ ! -d "$VENV_DIR" ]; then
    write_warning "run_lint" "Creating virtual environment..."
    python -m virtualenv "$VENV_DIR"
fi

# Activate the virtual environment
. "$VENV_DIR/bin/activate"

# Ensure virtual environment deactivation on script exit
function deactivate_virtualenv {
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
        write_warning "run_lint" "Virtual environment deactivated."
    fi
}
trap deactivate_virtualenv EXIT

# Ensure pylint is installed in the virtual environment
if ! pip show pylint &> /dev/null
then
    write_warning "run_lint" "pylint is not installed in the virtual environment. Installing..."
    pip install pylint
fi

# Check for existing pylintrc or create one
PYLINTRC_PATH="$CURRENT_SCRIPT_DIRECTORY_ENV/pylintrc"
if [ ! -f "$PYLINTRC_PATH" ]; then
    write_warning "run_lint" "pylintrc configuration file not found. Creating a basic pylintrc..."
    pylint --generate-rcfile > "$PYLINTRC_PATH"
fi

# Read ignored paths from .gitignore and format them for pylint
IGNORE_PATHS="venv"  # Include the virtual environment by default
if [ -f "$CURRENT_SCRIPT_DIRECTORY_ENV/.gitignore" ]; then
    IGNORED_FILES=$(grep -v '^#' "$CURRENT_SCRIPT_DIRECTORY_ENV/.gitignore" | grep -v '^$' | tr '\n' ',' | sed 's/,$//')
    IGNORE_PATHS="$IGNORE_PATHS,$IGNORED_FILES"
fi

# Define target directory or files for linting
TARGET_DIRECTORY="${1:-.}"

# Run pylint with the configuration file and ignored paths
write_info "run_lint" "Running pylint on $TARGET_DIRECTORY with pylintrc configuration, ignoring paths: $IGNORE_PATHS"
pylint --rcfile="$PYLINTRC_PATH" --ignore="$IGNORE_PATHS" "$TARGET_DIRECTORY"

# Display success message
write_success "run_lint" "Linting completed"
exit 0