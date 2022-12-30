
import os
import sys
from typing import List
from blog_tool.models.blog_collection import BlogCollection
from blog_tool.logging.blog_tool_logger import get_logger
import traceback
import rich_click as click
from blog_tool.utility.blogs.utility_blogs import create_blog, create_collection, get_blogs, get_collections, is_valid_blog, is_valid_collection
from blog_tool.utility.click.utility_click import write_debug, write_error, write_info, write_success
from blog_tool.utility.utility_exporters import get_exporter_modules_names
from blog_tool.utility.utility_names import create_id_from_name
from blog_tool.utility.utility_paths import get_default_collection_name, get_default_collections_path
from blog_tool.utility.utility_tests import get_tests_path


@cli_upload.command("blog", help="Publish a blog.")
@click.option("--blog-id", "-b", "blog_id", type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option("--collection-id", "-c", "collection_id", type=str, default="default", required=True, prompt=True, prompt_required=True)
@click.option("--collections-path", "-c", "collection_path", type=str, default=get_default_collections_path(), required=False)
@click.pass_context
def cli_upload_blog(ctx, blog_id: str, collection_id: str, collections_path: str):
    if not blog_id:
        raise ValueError("The blog ID is invalid or null")
    if not collection_id:
        raise ValueError("The collect ID is invalid or null")
    if not collections_path:
        raise ValueError("The collections path is invalid or null")

    if not is_valid_collection(collection_id, collections_path):
        write_error(f"The collection \"{collection_id}\" is not valid.")
        return 1
    if not is_valid_blog(blog_id, collection_id, collections_path):
        write_error(f"The blog \"{blog_id}\" is not valid.")
        return 2
    return 1
