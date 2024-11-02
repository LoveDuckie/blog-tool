#!/bin/bash
<<EOF

   Blog Tool \ Scripts \ Run Lint

   Run linting operations using pylint with a pylintrc configuration, within a virtual environment

EOF

CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

# Check if virtualenv is installed, install if not
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv is not installed. Installing..."
    pip install virtualenv
fi

# Create a virtual environment if it doesn't already exist
VENV_DIR="$CURRENT_SCRIPT_DIRECTORY_ENV/venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    virtualenv "$VENV_DIR"
fi

# Activate the virtual environment
. "$VENV_DIR/bin/activate"

# Ensure pylint is installed in the virtual environment
if ! pip show pylint &> /dev/null
then
    echo "pylint is not installed in the virtual environment. Installing..."
    pip install pylint
fi

# Check for existing pylintrc or create one
PYLINTRC_PATH="$CURRENT_SCRIPT_DIRECTORY_ENV/pylintrc"
if [ ! -f "$PYLINTRC_PATH" ]; then
    echo "pylintrc configuration file not found. Creating a basic pylintrc..."
    pylint --generate-rcfile > "$PYLINTRC_PATH"
fi

# Define target directory or files for linting
TARGET_DIRECTORY="${1:-.}"

# Run pylint with the configuration file
echo "Running pylint on $TARGET_DIRECTORY with pylintrc configuration..."
pylint --rcfile="$PYLINTRC_PATH" "$TARGET_DIRECTORY"

# Deactivate the virtual environment
deactivate

# Display success message
write_success "run_lint" "Linting completed"
