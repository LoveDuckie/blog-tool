from blog_tool.utility.paths.utility_paths import get_repo_root_path
import os


def get_default_storage_path() -> str:
    """Get the absolute path to the root of the repository

    Returns:
        str: The absolute path to the root of the repository
    """
    return get_repo_root_path()


def get_collections_path(storage_path: str = get_default_storage_path()) -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections.
    """
    return os.path.abspath(os.path.join(storage_path, "collections"))


def get_default_exported_path(*paths) -> str:
    """Get the default export path for exporting or rendering blogs out to.

    Returns:
        str: Returns the newly generaed path.
    """
    path_combined = os.sep.join(paths)
    return os.path.abspath(os.path.join(get_default_storage_path(), "exported", path_combined))


def get_default_collections_path() -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections.
    """
    return get_collections_path(get_default_storage_path())
