import os
from blog_tool.models.blog_collection import BlogCollection
from blog_tool.models.metadata.metadata_blog_collection import BlogCollectionMetadata
from blog_tool.utility.blogs.utility_blogs_validation import is_valid_collection
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_collections_path, get_default_metadata_path_name, get_default_storage_path
from blog_tool.utility.utility_names import create_id_from_name


def get_default_collection_metadata_filename() -> str:
    """The filename of the metadata file

    Returns:
        str: The filename of the metadata file
    """
    return "metadata-collection.json"


def get_default_collection_id() -> str:
    """Get the ID of the default collection

    Returns:
        str: The default collection ID
    """
    return "default"


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


def get_default_collection_path(
        collection_id=get_default_collection_id(),
        storage_path=get_default_storage_path()
) -> str:
    """Get the default absolute path to the collection

    Returns:
        str: Get the absolute path to the default collection.
    """
    return get_collection_path(storage_path, collection_id)


def get_collection_path(collection_id: str = get_default_collection_id(),
                        storage_path: str = get_default_storage_path()) -> str:
    """Get the absolute path to where the collection is stored on disk

    Args:
        storage_path (str): The absolute path to the root of the storage for blogs
        collection_id (str, optional): The ID for the collection. Defaults to get_default_collection_id().

    Raises:
        ValueError: If the collection ID is invalid or null
        ValueError: If the calculated collection path is invalid or null

    Returns:
        str: The absolute path to where the collection is stored on disk
    """
    if not collection_id:
        raise ValueError("The name of the collection is invalid or null")
    if collection_id := create_id_from_name(collection_id):
        return os.path.join(get_default_collections_path(storage_path), collection_id)
    else:
        raise ValueError("The slug name is invalid or null")


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
    if collection_id is None:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    return os.path.join(get_collection_path(storage_path, collection_id), get_default_metadata_path_name())


def get_collections(storage_path: str = get_default_storage_path()) -> list[BlogCollection]:
    """Get a list of blog collections

    Args:
        collections_path (str, optional): The absolute path to blog collections.. Defaults to get_default_collections_path().

    Raises:
        ValueError: The collections path specified is invalid or null
        IOError: The collections path does not exist.
        IOError: The collection path does not exist.

    Returns:
        list[BlogCollection]: A list of collections.
    """
    collections_path = get_default_collections_path(storage_path)
    if collections_path is None:
        raise ValueError("The path specified is invalid or null")

    if not os.path.exists(collections_path):
        raise IOError(
            f"The path \"{collections_path}\" does not exist. Unable to continue.")

    collections = []

    for collection_id in os.listdir(collections_path):
        collection_path = os.path.join(collections_path, collection_id)
        if not os.path.exists(collection_path):
            raise IOError(
                f"Failed: unable to find the path \"{collection_path}\"")

        if not is_valid_collection(collection_id, collections_path):
            raise Exception(
                f"The collection \"{collection_id}\" is not valid.")

        collection = BlogCollection(BlogCollectionMetadata.load(
            get_collection_metadata_filepath(collection_id, collections_path)))
        collections.append(collection)

    return collections
