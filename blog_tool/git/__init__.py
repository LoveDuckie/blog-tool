import subprocess
import os


def get_git_repo_root() -> str:
    """Get the absolute path to where the Git repository is on filesystem

    Raises:
        ValueError: When the retrieved path is considered null or invalid.

    Returns:
        str: The absolute path to the root of the git repository.
    """
    root_path = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'], check=True, stdout=subprocess.PIPE).stdout
    if root_path is None:
        raise ValueError(
            "The absolute path to the root of the repository is invalid or null")
    return root_path.decode("utf-8").strip()


def get_git_repo_path(*paths) -> str:
    """Generate the path from the root repository path

    Returns:
        str: The absolute path
    """
    return os.path.join(get_git_repo_root(), *paths)


def get_git_repo_branch_name() -> str:
    """Retrieve the active name of the Git repository branch

    Raises:
        ValueError: Raised if the branch name returned is invalid or null

    Returns:
        str: Returns the active branch name
    """
    branch_name = subprocess.run(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], check=True, stdout=subprocess.PIPE).stdout
    if branch_name is None:
        raise ValueError(
            "The name of the branch returned is invalid or null")
    return branch_name.decode("utf-8").strip()
