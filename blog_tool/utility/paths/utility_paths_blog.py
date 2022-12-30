import os
from blog_tool.utility.paths.utility_paths import get_repo_root
from blog_tool.utility.utility_names import create_id_from_name


def get_default_collection_name() -> str:
    return "default"


def get_default_collection_metadata_filename() -> str:
    return "blog_collection.json"


def get_default_blog_metadata_filename() -> str:
    return "blog.json"


def get_default_metadata_path_name() -> str:
    """Get the default name to use for storing metadata about the the blog or collection

    Returns:
        str: The metadata path name.
    """
    return ".metadata"


def get_default_blogs_path(repo_root: str = None) -> str:
    """Returns the default path to where the blogs are stored in the repository.

    Returns:
        str: The absolute path to where the blogs are stored in the repository.
    """
    return os.path.abspath(os.path.join(get_repo_root(), "blogs"))


def get_default_collections_path(repo_root: str = None) -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections.
    """
    return os.path.abspath(os.path.join(get_default_blogs_path(repo_root), "collections"))


def get_default_collection_path() -> str:
    """Get the default absolute path to the collection

    Returns:
        str: Get the absolute path to the default collection.
    """
    return get_collection_path(get_default_collection_name())


def get_collection_path(repo_root: str, collection_id: str = get_default_collection_name()) -> str:
    if not collection_id:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    if not collection_id:
        raise ValueError("The slug name is invalid or null")
    return os.path.join(get_default_collections_path(repo_root), collection_id)


def get_collection_metadata_path(
        collection_id: str = get_default_collection_name(),
        collections_path: str = get_default_collections_path()) -> str:
    if collection_id is None:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    return os.path.join(collections_path, collection_id, get_default_metadata_path_name())


def get_collection_metadata_filepath(
        collection_id: str = get_default_collection_name(),
        collections_path: str = get_default_collections_path()) -> str:
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")
    return os.path.join(get_collection_metadata_path(collection_id, collections_path), "collection.json")


def get_blog_path(blog_id: str, collection_id: str = None, collections_path: str = get_default_collections_path()) -> str:
    collection_id = collection_id if collection_id is not None else get_default_collection_name()
    return os.path.join(get_collection_path(collection_id, collections_path), blog_id)


def get_blog_metadata_path(blog_id: str, collection_id: str = get_default_collection_name(),
                           collections_path: str = get_default_collections_path()) -> str:
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    return os.path.join(get_blog_path(blog_id, collection_id, collections_path), get_default_metadata_path_name())


def get_blog_metadata_filepath(
        blog_id: str, collection_id: str = get_default_collection_name(),
        collections_path: str = get_default_collections_path()) -> str:
    """Get the absolute file path to where the metadata file is for a blog

    Args:
        blog_id (str): The ID for a blog
        collection_id (str, optional): The ID for a collection. Defaults to get_default_collection_name().
        collections_path (str, optional): The absolute path to where the collections are stored. Defaults to get_default_collections_path().

    Raises:
        ValueError: If the blog ID was not defined
        ValueError: If the collection ID was not defined

    Returns:
        str: The absolute file path to the blog meta data
    """
    if not blog_id:
        raise ValueError("The ID of the blog is invalid or null")
    if not collection_id:
        raise ValueError("The ID of the collection is invalid or null")

    return os.path.join(get_blog_metadata_path(blog_id, collection_id, collections_path), "blog.json")


def get_default_export_path(*paths) -> str:
    """Get the default export path for exporting or rendering blogs out to.

    Returns:
        str: Returns the newly generaed path.
    """
    path_combined = os.sep.join(paths)
    return os.path.abspath(os.path.join(get_repo_root(), "exported", path_combined))


def get_blog_export_path(blog_id: str, collection_id: str = get_default_collection_name(),
                         collections_path: str = get_default_collections_path()) -> str:
    if blog_id is None:
        raise ValueError("The blog is not considered valid.")
    if collection_id is None:
        raise ValueError("The collection is not considered valid.")

    return get_default_export_path("collections", collection_id, "blogs", blog_id)
