import os
from blog_tool.models.blog import Blog, BlogMetadata
from blog_tool.models.blog_collection import BlogCollection, BlogCollectionMetadata
from blog_tool.utility.blogs.utility_blogs_validation import is_valid_collection
from blog_tool.utility.paths.utility_paths_blog_storage import get_default_collections_path, get_default_storage_path
from blog_tool.utility.utility_names import create_id_from_name

from blog_tool.utility.paths.utility_paths_blog import get_blog_metadata_filepath, get_blog_path, get_collection_metadata_filepath, get_collection_path, get_default_collection_id, get_repo_root, get_repo_root

_collection_dirs = ['.metadata', 'assets', 'blogs']
_blog_dirs = ['.metadata', 'assets']


def create_blog_paths(target_path: str) -> None:
    """Create the paths for a new blog at the target path specified.

    Args:
        target_path (str): The absolute path to the directory to create the paths in

    Raises:
        ValueError: The absolue target path is invalid or null
        IOError: The absolute target path does not exist
    """
    global _blog_dirs
    if target_path is None:
        raise ValueError("The path was not specified. Unable to continue.")

    if not os.path.isabs(target_path):
        raise IOError(
            f"The path \"{target_path}\" is not an absolute path. Unable to continue.")

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for path in _blog_dirs:
        new_path = os.path.join(target_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_collections_paths(target_path: str) -> None:
    """Create the paths for the collection

    Args:
        target_path (str): The absolute path to the target directory

    Raises:
        ValueError: If the target path was not defined.
    """
    global _collection_dirs
    if target_path is None:
        raise ValueError("The target path is invalid or null")

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for path in _collection_dirs:
        os.makedirs(os.path.join(target_path, path))


def create_blog_metadata_file(
        blog_id: str, collection_id: str, collections_path: str = get_repo_root(),
        **kwargs) -> BlogMetadata:
    """Return the newly instantiated blog metadata file

    Args:
        blog_id (str): The ID for the blog
        collection_id (str): The collecti onf othe blog
        collections_path (str, optional): The absolute path to where the collections are stored. Defaults to get_repo_root().

    Raises:
        ValueError: If the blog Id is invalid or null
        ValueError: If the collection ID is invalid or null
        IOError: If the collections path does not exist
        ValueError: If the blog is invalid or null

    Returns:
        BlogMetadata: The instantiated blog metadata model
    """
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null.")

    if collection_id is None:
        raise ValueError("The collection ID is invalid or null.")

    if not os.path.exists(collections_path):
        raise IOError(f"The path \"{collections_path}\" does not exist.")

    blog_path = get_blog_path(blog_id, collection_id, collections_path)
    if not os.path.exist(blog_path):
        os.makedirs(blog_path)

    blog = BlogMetadata.create(os.path.dirname(get_blog_metadata_filepath(
        blog_id, collection_id, collections_path)), **kwargs)
    if blog is None:
        raise ValueError("The blog is invalid or null")

    return blog


def create_blog(
        blog_id: str, collection_id: str = get_default_collection_id(),
        collections_path: str = get_repo_root(),
        **kwargs):
    global _blog_dirs
    if not blog_id:
        raise ValueError("The blog ID is invalid or null")
    blog_path = get_blog_path(blog_id, collection_id, collections_path)

    if not os.path.exists(blog_path):
        os.makedirs(blog_path)

    blog_slug = create_id_from_name(blog_id)
    if blog_slug is None or blog_slug == '':
        raise ValueError("The blog slug name is invalid or null")

    create_blog_paths(get_blog_path(blog_id, collection_id))
    create_blog_metadata_file()


def get_blogs(collection_id: str = get_default_collection_id(),
              collections_path: str = get_repo_root()) -> list:
    blogs = []

    collection_path = get_collection_path(collection_id, collections_path)
    metadata_filepath = get_collection_metadata_filepath(
        collection_id, collections_path)
    if metadata_filepath is None:
        raise ValueError("The metadata filepath is invalid or null")

    if not os.path.exists(metadata_filepath):
        raise IOError(
            f"Failed: unable to find the file \"{metadata_filepath}\"")

    for blog_id in os.listdir(collection_path):
        blog_metadata_filepath = get_blog_metadata_filepath(
            blog_id, collection_id, collections_path)

        blog_metadata = BlogMetadata.load(blog_metadata_filepath)
        blogs.append(Blog(blog_metadata))

    return blogs
