#!/usr/bin/env bash
<<EOF

   Blog Tool \ Generate \ Documentation

   Generate documentation for the project

EOF

CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV/scripts)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

write_info "run_generate_docs" "Install: Python Version \"$(<$CURRENT_SCRIPT_DIRECTORY_ENV/.python-version)\""
pyenv install --skip-existing
if ! write_response "run_generate_docs" "Install: Python Version"; then
    write_error "run_generate_docs" "Failed: Unable to install target Python version"
    exit 1
fi

# Check if virtualenv is installed, install if not
if ! python -m virtualenv --version &> /dev/null
then
    write_warning "run_generate_docs" "\"virtualenv\" is not installed. Installing..."
    python -m pip install virtualenv
fi

# Create a virtual environment if it doesn't already exist
VENV_DIR="$CURRENT_SCRIPT_DIRECTORY_ENV/venv"
if [ ! -d "$VENV_DIR" ]; then
    write_warning "run_generate_docs" "Creating virtual environment..."
    python -m virtualenv "$VENV_DIR"
fi

# Activate the virtual environment
. "$VENV_DIR/bin/activate"

# Ensure the virtual environment is deactivated after the script ends
function deactivate_virtualenv {
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
        write_warning "run_generate_docs" "Virtual environment deactivated."
    fi
}
trap deactivate_virtualenv EXIT

# Step 1: Install Sphinx and dependencies
write_info "run_generate_docs" "Checking and installing Sphinx and dependencies if needed..."
pip show sphinx >/dev/null 2>&1 || pip install sphinx sphinx-rtd-theme || { write_error "run_generate_docs" "Failed to install Sphinx"; exit 1; }

# Step 2: Set up docs directory
DOCS_DIR="docs"
SRC_DIR="src"  # Adjust if your source code is in a different directory

if [ ! -d "$DOCS_DIR" ]; then
    write_info "run_generate_docs" "Creating docs directory..."
    mkdir -p "$DOCS_DIR"
else
    write_info "run_generate_docs" "Docs directory already exists."
fi

cd "$DOCS_DIR" || { write_error "run_generate_docs" "Failed to access docs directory"; exit 1; }

# Step 3: Initialize Sphinx configuration if not present
if [ ! -f "conf.py" ]; then
    write_info "run_generate_docs" "Initializing Sphinx configuration..."
    sphinx-quickstart --quiet --project "Blog Tool" --author "Luc Shelton" --release "0.1.0" --makefile --batchfile || { write_error "run_generate_docs" "Sphinx initialization failed"; exit 1; }
else
    write_info "run_generate_docs" "Sphinx configuration (conf.py) already exists. Skipping initialization."
fi

# Step 4: Check and update conf.py with additional extensions if necessary
if ! grep -q "sphinx.ext.autodoc" conf.py; then
    write_info "run_generate_docs" "Configuring Sphinx with extensions..."
    cat >> conf.py << EOL

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',     # Automatic documentation generation from docstrings
    'sphinx.ext.napoleon',    # Google and NumPy style docstring support
    'sphinx.ext.viewcode',    # Links to highlighted source code
]

# HTML Theme
html_theme = 'sphinx_rtd_theme'

# Path setup
import os
import sys
sys.path.insert(0, os.path.abspath('../$SRC_DIR'))  # Modify to point to your source directory if different
EOL
else
    write_info "run_generate_docs" "Sphinx extensions already configured in conf.py."
fi

# Step 5: Generate .rst files using autodoc if not already present
if [ ! -f "index.rst" ]; then
    write_info "run_generate_docs" "Generating .rst files with sphinx-apidoc..."
    sphinx-apidoc -o . "../$SRC_DIR" || { write_error "run_generate_docs" "sphinx-apidoc failed"; exit 1; }
else
    write_info "run_generate_docs" "Sphinx .rst files already generated. Skipping sphinx-apidoc."
fi

# Step 6: Build HTML documentation
write_info "run_generate_docs" "Building HTML documentation..."
make html || { write_error "run_generate_docs" "HTML build failed"; exit 1; }

write_success "run_generate_docs" "Documentation generated successfully. Open docs/_build/html/index.html to view it."
exit 0
