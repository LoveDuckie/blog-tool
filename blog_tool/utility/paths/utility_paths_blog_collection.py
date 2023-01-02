

from blog_tool.utility.paths.utility_paths_blog import get_default_blogs_path, get_default_collection_id, get_default_collection_metadata_filename, get_default_metadata_path_name, get_default_storage_path
import os
from blog_tool.utility.utility_names import create_id_from_name


def get_collection_metadata_filepath(
        collection_id: str = get_default_collection_id(),
        storage_path: str = get_default_storage_path()) -> str:
    """Retrieve the absolute path to the metadata file

    Args:
        collection_id (str, optional): The ID for the collection. Defaults to get_default_collection_id().
        storage_path (str, optional): The absolute path for storage. Defaults to get_default_storage_path().

    Raises:
        ValueError: If the collection ID is invalid or null
        ValueError: If the storage path is invalid or null

    Returns:
        str: The absolute path to where the metadata file is stored.
    """
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if storage_path is None:
        raise ValueError("The collections path is invalid or null")
    return os.path.join(
        get_collection_metadata_path(collection_id, storage_path),
        get_default_collection_metadata_filename())


def get_default_storage_path(storage_path: str = get_default_storage_path()) -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections.
    """
    return os.path.abspath(os.path.join(get_default_blogs_path(storage_path), "collections"))


def get_default_collection_path(
        storage_path=get_default_storage_path(),
        collection_id=get_default_collection_id()) -> str:
    """Get the default absolute path to the collection

    Returns:
        str: Get the absolute path to the default collection.
    """
    return get_collection_path(storage_path, collection_id)


def get_collection_path(storage_path: str, collection_id: str = get_default_collection_id()) -> str:
    if not collection_id:
        raise ValueError("The name of the collection is invalid or null")
    if collection_id := create_id_from_name(collection_id):
        return os.path.join(get_collections_path(storage_path), collection_id)
    else:
        raise ValueError("The slug name is invalid or null")


def get_collection_metadata_path(storage_path: str = get_default_storage_path(),
                                 collection_id: str = get_default_collection_id()) -> str:
    if collection_id is None:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    return os.path.join(get_collection_path(storage_path, collection_id), get_default_metadata_path_name())
