#!/bin/bash
<<EOF

   Blog Tool \ Setup \ Python Environment Manager

   Script for installing Python Environment Manager

EOF
CURRENT_SCRIPT_DIRECTORY_ENV=$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))
export SHARED_SCRIPTS_PATH_ENV=${SHARED_SCRIPTS_PATH_ENV:-$(realpath $CURRENT_SCRIPT_DIRECTORY_ENV)}
export CURRENT_SCRIPT_FILENAME=$(basename ${BASH_SOURCE[0]:-${(%):-%x}})
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_SCRIPTS_PATH_ENV/shared_functions.sh"
write_header

export DEFAULT_PYTHON_VERSION=3.10.0
export DEBIAN_FRONTEND=noninteractive
apt -yqq install make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
   libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

write_info "setup-tooling-pyenv" "installing python environment manager"
curl https://pyenv.run | bash
if ! write_response "setup-tooling-pyenv" "install python environment manager"; then
   write_error "setup-tooling-pyenv" "failed to install python environment manager"
   exit 1
fi

cat <<EOF >>~/.profile
export PYENV_ROOT="\$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="\$PYENV_ROOT/bin:\$PATH"
eval "\$(pyenv init -)"
EOF

write_info "setup-tooling-pyenv" "reloading environment"
. ~/.profile
eval "$(pyenv init -)"

write_info "setup-tooling-pyenv" "installing: python $DEFAULT_PYTHON_VERSION"
pyenv install $DEFAULT_PYTHON_VERSION
pyenv global $DEFAULT_PYTHON_VERSION
python -v

write_success "setup-tooling-pyenv" "done"
exit 0