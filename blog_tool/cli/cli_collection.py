import os
import sys
from typing import List
from blog_tool.models.blog_collection import BlogCollection
from blog_tool.logging.blog_tool_logger import get_logger
import traceback
import rich_click as click
from blog_tool.utility.utility_blogs import create_blog, create_collection, get_blogs, get_collections, is_valid_blog, is_valid_collection
from blog_tool.utility.utility_click import write_debug, write_error, write_info, write_success
from blog_tool.utility.utility_exporters import get_exporter_modules_names
from blog_tool.utility.utility_names import create_id_from_name
from blog_tool.utility.utility_paths import get_default_collection_name, get_default_collections_path
from blog_tool.utility.utility_tests import get_tests_path


@click.group("collection", help="Commands for managing a collection of blogs.")
@click.option("--collection-id", "-c", "collection_id", type=str, required=False, default=get_default_collection_name(),
              help="The ID of the blog collection.")
@click.option("--collection-path", "-p", "collections_path", type=str, required=False,
              default=get_default_collections_path(),
              help="The path to where the collections are stored.")
@click.pass_context
def cli_collection(ctx, collection_id: str, collections_path: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")

    ctx.obj['collection_id'] = collection_id
    ctx.obj['collections_path'] = collections_path

    write_success("Done")


@cli_collection.command("list", help="List all the collections.")
@click.option("--short", "-s", "short", is_flag=True, required=False,
              help="Display a shorter output from the list of collections.")
@click.pass_context
def cli_collection_list(ctx, short: bool):
    collections_path = ctx.obj['collections_path']
    collections: List[BlogCollection] = get_collections(collections_path)
