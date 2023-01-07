import os
from blog_tool.utility.paths.utility_paths_blog_collection import get_default_collection_id
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_storage_path, get_default_exported_path, get_blog_path
from blog_tool.utility.paths.utility_paths_storage import get_blog_path
from blog_tool.utility.paths.utility_paths import get_default_metadata_path_name


def get_default_blog_metadata_filename() -> str:
    """Get the default filename for the metadata file for the blog

    Returns:
        str: The default metadata file name
    """
    return "metadata-blog.json"


def get_blog_metadata_path(blog_id: str, collection_id: str = get_default_collection_id(),
                           storage_path: str = get_default_storage_path()) -> str:
    """Get the absolute path to where the metadata is stored for the blog

    Args:
        blog_id (str): The blog ID
        collection_id (str, optional): The collection ID for the blog. Defaults to get_default_collection_id().
        collections_path (str, optional): The absolute path to where the collections are stored. Defaults to get_default_collections_path().

    Raises:
        ValueError: If the blog ID is null
        ValueError: If the collection ID is null

    Returns:
        str: The absolute path to where the blog metadata is stored
    """
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    return os.path.abspath(os.path.join(
        get_blog_path(blog_id, collection_id, storage_path),
        get_default_metadata_path_name()))


def get_blog_metadata_filepath(
        blog_id: str, collection_id: str = get_default_collection_id(),
        storage_path: str = get_default_storage_path()) -> str:
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

    return os.path.join(
        get_blog_metadata_path(blog_id, collection_id, storage_path),
        get_default_blog_metadata_filename())


def get_blog_exported_path(blog_id: str, collection_id: str = get_default_collection_id()) -> str:
    """Retrieve the absolute path to where the blog is to be exported

    Args:
        blog_id (str): The ID for the blog
        collection_id (str, optional): The ID for the collection. Defaults to get_default_collection_id().

    Raises:
        ValueError: If the blog ID is invalid or null
        ValueError: If the collection ID is invalid or null

    Returns:
        str: The absolute path to where the blogs are to be exported.
    """
    if blog_id is None:
        raise ValueError("The blog is not considered valid.")
    if collection_id is None:
        raise ValueError("The collection is not considered valid.")

    return get_default_exported_path("collections", collection_id, "blogs", blog_id)
