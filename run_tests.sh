#!/usr/bin/env bash
<<EOF

   Project \ Tests \ Run with Coverage

   Run unit tests with coverage and generate a report

EOF

# Set up environment paths
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV/scripts)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
VENV_DIR="$CURRENT_SCRIPT_DIRECTORY_ENV/venv"

# Create and activate virtual environment if not already present
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Ensure virtual environment deactivation on script exit
function deactivate_virtualenv {
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
        echo "Virtual environment deactivated."
    fi
}
trap deactivate_virtualenv EXIT

# Check if coverage is installed, install if not
if ! pip show coverage &> /dev/null; then
    echo "Installing coverage..."
    pip install coverage
fi

# Run tests with coverage
write_info "run_tests" "Running unit tests with coverage..."
coverage run -m unittest discover || { write_error "run_tests" "Unit tests failed"; exit 1; }

# Generate and display the coverage report
write_info "run_tests" "Generating coverage report..."
coverage report -m

# Optional: Generate an HTML coverage report
coverage html
write_info "run_tests" "Coverage HTML report generated at htmlcov/index.html"

write_success "run_tests" "Unit tests completed with coverage."
exit 0