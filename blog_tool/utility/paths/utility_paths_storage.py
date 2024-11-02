import os
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_storage_path, get_collections_path
from blog_tool.utility.utility_names import create_id_from_name


def get_default_collection_id() -> str:
    """Get the ID of the default collection

    Returns:
        str: The default collection ID
    """
    return "default"


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
    if not storage_path:
        raise ValueError("The storage path specified is invalid or null")
    if not os.path.isabs(storage_path):
        raise ValueError(f"The path \"{storage_path}\" is not an absolute path.")
    if not collection_id:
        raise ValueError("The name of the collection is invalid or null")
    if collection_id := create_id_from_name(collection_id):
        return os.path.abspath(os.path.join(get_collections_path(storage_path), collection_id))
    else:
        raise ValueError("The slug name is invalid or null")


def get_blog_path(blog_id: str, collection_id: str = get_default_collection_id(),
                  storage_path: str = get_default_storage_path()) -> str:
    """Get the absolute path to where the blog and its associated data is stored

    Args:
        storage_path:
        blog_id (str): The ID for the blog
        collection_id (str, optional): The ID for the collection. Defaults to get_default_collection_id().
        collections_path (str, optional): The absolute path to where the collections are sdtored. Defaults to get_default_collections_path().

    Returns:
        str: _description_
    """
    if not blog_id:
        raise ValueError("The blog ID is invalid or null")
    blog_id = create_id_from_name(blog_id)
    if collection_id := create_id_from_name(collection_id):
        return os.path.abspath(os.path.join(get_collection_path(collection_id, storage_path), blog_id))
    else:
        raise ValueError("The instantiated collection ID is invalid or null")
