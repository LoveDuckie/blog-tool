import os
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_storage_path, get_collections_path
from blog_tool.utility.paths.utility_paths_blog_collection import get_collection_metadata_filepath, get_collection_path, get_default_collection_id
from blog_tool.models.blog_collection import BlogCollection
from blog_tool.utility.blogs.utility_blogs_validation import is_valid_collection
from blog_tool.models.blog_collection import BlogCollectionMetadata
from blog_tool.utility.utility_names import create_id_from_name


def delete_collection(collection_id: str, storage_path: str = get_default_storage_path()):
    if not collection_id:
        raise ValueError("The collection ID is invalid or null")
    if not storage_path:
        raise ValueError("The absolute path to where the blogs are stored on disk")
    return


def create_collection(
        collection_id: str = get_default_collection_id(),
        storage_path: str = get_default_storage_path(),
        **kwargs):
    """Create the blog collection

    Args:
        collection_name (str): The name or slug name of the collection
        collections_path (str, optional): The absolute path to where the blog collections are. Defaults to get_default_collections_path().

    Raises:
        ValueError: The collection name is invalid or null.
        ValueError: The blog collection is not considered valid.
    """
    global _collection_dirs
    if collection_id is None:
        raise ValueError("The collection name is invalid or null")

    collection_id = create_id_from_name(collection_id)

    if not is_valid_collection(collection_id, storage_path):
        raise Exception(f"The \"{collection_id}\" already exists.")

    collection_path = get_collection_path(collection_id, storage_path)

    if not os.path.exists(collection_path) and not kwargs['force']:
        os.makedirs(collection_path)

    for path in _collection_dirs:
        new_path = os.path.join(collection_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    create_collection_metadata_file(collection_id, storage_path, **kwargs)


def create_collection_metadata_file(
        collection_id: str, storage_path: str = get_default_storage_path(),
        **kwargs) -> BlogCollectionMetadata:
    if collection_id is None:
        raise ValueError("The collection name is invalid or null")

    if not is_valid_collection(collection_id, storage_path):
        create_collection(collection_id, storage_path)

    collection_path = get_collection_path(collection_id, storage_path)
    if not collection_path:
        raise ValueError(
            "The absolute path to the collection is invalid or null")

    collection_metadata_filepath = get_collection_metadata_filepath(
        collection_id, storage_path)
    collection_metadata_path = os.path.dirname(collection_metadata_filepath)
    if not os.path.exists(collection_metadata_path):
        os.makedirs(collection_metadata_path)

    if collection_metadata := BlogCollectionMetadata.create(
        collection_metadata_filepath, **kwargs
    ):
        return collection_metadata
    else:
        raise ValueError("The collection metadata is invalid or null")


def get_collection(collection_id: str, storage_path: str = get_default_storage_path()) -> BlogCollection:
    """Retrieve the instantiated collection

    Args:
        collection_id (str): The ID for the collection to load
        collections_path (str, optional): The absolute path to where the collections are stored. Defaults to get_repo_root().

    Raises:
        ValueError: If the collection ID is invalid or null
        ValueError: If the absolute path to where the colletions are stored is invalid or null
        IOError: If the collections metadata file is invalid or null
        ValueError: If the collection metadata model loaded is invalid or null

    Returns:
        BlogCollection: The instantiated blog collection.
    """
    collections_path = get_collections_path(storage_path)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    if collections_path is None:
        raise ValueError("The collections path specified is invalid or null")

    collection_metadata_filepath = get_collection_metadata_filepath(
        collection_id, collections_path)

    if not os.path.exists(collection_metadata_filepath):
        raise IOError(f"Failed: unable to find metadata filepath \"{collection_metadata_filepath}\"")
    collection_metadata = BlogCollectionMetadata.load(
        collection_metadata_filepath)
    if collection_metadata is None:
        raise ValueError("The collection metadata is invalid or null")

    return BlogCollection(collection_metadata)


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
    collections_path = get_collections_path(storage_path)
    if collections_path is None:
        raise ValueError("The path specified is invalid or null")

    if not os.path.exists(collections_path):
        raise IOError(
            f"The path \"{collections_path}\" does not exist. Unable to continue.")

    collections = []

    for collection_id in os.listdir(collections_path):
        collection_path = get_collection_path(collection_id, storage_path)
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
