import os
import subprocess
from blog_tool.utility.paths.utility_paths_config import get_default_config_filename, get_default_user_config_filename
from blog_tool import __title__, __project__
import pathlib

_repo_root = None


def get_package_root():
    """Get the absolute path to the root of the project

    Returns:
        str: The absolute path to the root of of the project
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_package_path(*paths) -> str:
    """Generate the project path based on the elements specified in the list

    Returns:
        str: The absolute path
    """
    return os.path.join(get_package_root(), *paths)


def get_default_package_config_filepath() -> str:
    """Get the absolute path to the default configuration file

    Returns:
        str: The absolute path to the default configuration file
    """
    return os.path.join(get_package_root(), __project__, "data", "config", get_default_config_filename())


def get_default_user_path() -> str:
    """Generate and return the default path to where user configurations are stored.

    Returns:
        str: The absolute path to where user configurations are stored.
    """
    return os.path.join(pathlib.Path.home(), __title__)


def get_default_user_config_filepath() -> str:
    """Get the default user configuration file path
+F
    Returns:
        str: Returns the absolute path to the user configuration path
    """
    return os.path.join(get_default_user_path(), "config", get_default_user_config_filename())


def _create_repo_root() -> str:
    """Resolve the absolute path to the root of the repository.

    Returns:
        str: The absolute path to the root of the repository.
    """
    process = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('ascii').rstrip()


def get_repo_root() -> str:
    """Get the absolute path to the root of the Git repository.

    Returns:
        str: Returns the absolute path of the Git repository.
    """
    global _repo_root

    if _repo_root is None:
        _repo_root = _create_repo_root()
    return _repo_root


def get_repo_root_path(*paths) -> str:
    """Get the absolute path to the newly generated path.

    Returns:
        str: Returns the absolute path.
    """
    return os.path.join(get_repo_root(), *paths)


def get_default_metadata_path_name() -> str:
    """Get the default name to use for storing metadata about the the blog or collection

    Returns:
        str: The metadata path name.
    """
    return ".metadata"
