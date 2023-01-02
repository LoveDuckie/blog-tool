import os
from blog_tool.utility.paths.utility_paths_blog import get_collection_path, get_default_collection_id, get_default_collections_path


def is_valid_collection(collection_id: str = get_default_collection_id(),
                        storage_path: str = get_default_collections_path()) -> bool:
    if collection_id is None or not collection_id:
        raise ValueError("The blog collection ID is invalid or null")

    if not os.path.exists(storage_path):
        return False

    if collection_path := get_collection_path(storage_path, collection_id):
        return bool(os.path.exists(collection_path))
    else:
        raise ValueError("The collection path is invalid or null")


def is_valid_blog(blog_id: str, collection_id: str = get_default_collection_id(),
                  collections_path: str = get_default_collections_path()) -> bool:
    # sourcery skip: raise-specific-error
    if blog_id is None:
        raise ValueError("The blog slug name is invalid or null")

    if not is_valid_collection(collection_id):
        raise Exception("The blog collection slug name is invalid or null")

    collection_path = get_collection_path(collection_id, collections_path)
    if not os.path.exists(collection_path):
        return False

    collection_metadata_filepath = os.path.join(
        collection_path, "collection.json")

    return bool(os.path.exists(collection_metadata_filepath))
