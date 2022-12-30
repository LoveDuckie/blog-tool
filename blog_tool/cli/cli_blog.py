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


@click.group("blog", help="Manage singular blogs.")
@click.option("--collection-id", "-c", "collection_id", type=str, required=False, default=get_default_collection_name(),
              help="The ID of the blog collection.")
@click.option("--collection-path", "-p", "collections_path", type=str, required=False,
              default=get_default_collections_path(),
              help="The path to where the collections are stored.")
@click.pass_context
def cli_blogs(ctx, collection_id: str, collections_path: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")

    ctx.obj['collection_id'] = collection_id
    ctx.obj['collections_path'] = collections_path

    write_success("Done")


@cli_blogs.command("create", help="Create a new blog in a collection.")
@click.option("--blog-id", "-i", "blog_id", type=str, default=None, required=False, prompt_required=True,
              prompt="Blog ID", help="The ID of the blog to create.")
@click.option("--blog-name", "-n", "blog_name", type=str, default=None, required=True, prompt_required=True,
              prompt="Blog Name", help="The name of the blog to create.")
@click.option("--blog-description", "-d", "blog_description", type=str, default=None, required=False,
              prompt_required=True, prompt="Blog Description", help="The description of the blog to create.")
@click.option("--tag", "-t", "blog_tags", type=str, multiple=True, default=[],
              required=False, prompt_required=True, prompt="Blog Tags", help="The associative tags with this blog.")
@click.pass_context
def cli_blogs_create(ctx, blog_id: str, blog_name: str, blog_description: str, blog_tags: List[str]):
    if blog_id is None:
        raise ValueError(
            "The name of the blog is invalid or null. Unable to continue.")

    collection_id: str = ctx.obj['collection_id']
    blog_id: str = create_id_from_name(blog_id)
    write_info(f"Creating: \"{blog_id}\"")
    try:
        create_blog(blog_id, collection_id, name=blog_name,
                    description=blog_description, tags=blog_tags)
    except Exception as exc:
        tb = traceback.format_exc()
        write_error(tb)

    write_success("Done")


@cli_blogs.command("delete", help="Delete an existing blog from a collection.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_delete(ctx, blog_id: str):
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    collection_id = ctx.obj['collection_id']
    collections_path = ctx.obj['collections_path']

    if not is_valid_blog(blog_id, collection_id, collections_path):
        write_error(f"The blog \"{blog_id}\" is not valid.")
    write_success("Done")


@cli_blogs.command("validate", help="Delete an existing blog from a collection.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_delete(ctx, blog_id: str):
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    collection_id = ctx.obj['collection_id']
    collections_path = ctx.obj['collections_path']

    if not is_valid_blog(blog_id, collection_id, collections_path):
        write_error(f"The blog \"{blog_id}\" is not valid.")
    write_success("Done")
