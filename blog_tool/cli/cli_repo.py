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


@click.group("repo", help="Modify the behaviour of the blog_tool tool.")
@click.pass_context
def cli_repo(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_repo.command("init", help="Initialise the repository at the path specified.")
@click.option("--path", "-p", "path", type=str, default="",
              help="The absolute path to where the repository is located.")
@click.pass_context
def cli_repo_init(ctx, path: str):
    pass


@cli_repo.command("validate", help="Initialise the repository at the path specified.")
@click.option("--path", "-p", "path", type=str, default="",
              help="The absolute path to where the repository is located.")
@click.pass_context
def cli_repo_validate(ctx, path: str):
    pass
