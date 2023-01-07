import pkgutil
from typing import List
from blog_tool import image_uploaders
from blog_tool.utility.blogs.utility_blogs import is_valid_collection
from blog_tool.utility.paths.utility_paths_blog_collection import get_default_collection_name, get_default_collections_path
from blog_tool.utility.blogs.utility_blogs import is_valid_blog
import os

from blog_tool.utility.paths.utility_paths_blog_storage import get_default_storage_path


def get_image_uploader_modules() -> List:
    """Get the list of modules for uploads

    Returns:
        list: Returns a list of module names for uploader interfaces.
    """
    return list(
        map(
            lambda x: x.name,
            filter(
                lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules(
                    [os.path.dirname(image_uploaders.__file__)]))))


def upload_collection(collection_id: str = get_default_collection_name(),
                      storage_path: str = get_default_storage_path()):
    """Upload all the blogs in the collection specified

    Args:
        collection_id (str, optional): The ID for the collection. Defaults to get_default_collection_name().
        collections_path (str, optional): The path to where the collections are stored. Defaults to get_default_collections_path().

    Raises:
        ValueError: If the collection ID is invalid or null
        Exception: If the collection ID specified is considered valid (exists on disk)
    """
    if collection_id is None:
        raise ValueError("The collection is invalid or null")
    if not is_valid_collection(collection_id):
        raise Exception(
            f"The collection \"{collection_id}\" is not valid. Unable to continue.")


def upload_blog(blog_id: str, collection_id: str = get_default_collection_name(),
                storage_path: str = get_default_storage_path()):
    # sourcery skip: raise-specific-error
    if not is_valid_blog(blog_id, collection_id, get_default_collections_path(storage_path)):
        raise Exception(
            f"The blog \"{blog_id}\" is not valid. Check that it exists, and try again.")
