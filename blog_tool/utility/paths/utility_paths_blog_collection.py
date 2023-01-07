import os
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_storage_path
from blog_tool.utility.paths.utility_paths_storage import get_collection_path, get_default_collection_id
from blog_tool.utility.paths.utility_paths import get_default_metadata_path_name
from blog_tool.utility.utility_names import create_id_from_name


def get_default_collection_metadata_filename() -> str:
    """The filename of the metadata file

    Returns:
        str: The filename of the metadata file
    """
    return "metadata-collection.json"


def get_default_collection_path(
    collection_id=get_default_collection_id()
) -> str:
    """Get the default absolute path to the collection

    Returns:
        str: Get the absolute path to the default collection.
    """
    return get_collection_path(collection_id, get_default_storage_path())


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
    if not storage_path:
        raise ValueError("The storage path specified is invalid or null")
    if not os.path.isabs(storage_path):
        raise ValueError(f"The path \"{storage_path}\" is not an absolute path.")
    return os.path.join(
        get_collection_metadata_path(collection_id, storage_path),
        get_default_collection_metadata_filename())


def get_collection_metadata_path(
    collection_id: str = get_default_collection_id(),
    storage_path: str = get_default_storage_path()
) -> str:
    """Retrieve the absolute path to where the metadata is stored for hte collection

    Args:
        storage_path (str, optional): The absolute path for storage. Defaults to get_default_storage_path().
        collection_id (str, optional): The ID of the collection we are retrieving the storage path for. Defaults to get_default_collection_id().

    Raises:
        ValueError: The collection ID was not defined.

    Returns:
        str: The absolute path to where collections are stored.
    """
    if not storage_path:
        raise ValueError("The storage path specified is invalid or null")
    if not os.path.isabs(storage_path):
        raise ValueError(f"The path \"{storage_path}\" is not an absolute path.")
    if collection_id is None:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    return os.path.join(get_collection_path(collection_id, storage_path), get_default_metadata_path_name())
