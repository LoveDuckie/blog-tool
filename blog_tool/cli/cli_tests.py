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


@click.group("tests", help="Modify the behaviour of the blog_tool tool.")
@click.pass_context
def cli_tests(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_tests.command("run", help="Run all available tests.")
@click.pass_context
def cli_tests_run(ctx):
    pass


@cli_tests.command("list", help="List all available tests that can be used")
@click.option("--path", "-p", "path", type=str, default=get_tests_path(),
              help="The absolute path to where unit tests are defined.")
@click.pass_context
def cli_tests_list(ctx, path: str):
    if not path:
        raise ValueError("The tests path is invalid or null")

    if not os.path.isabs(path):
        raise IOError(f"Failed: the path \"{path}\" is invalid.")

    if not os.path.exists(path):
        raise IOError(f"Failed: unable to find the tests \"{path}\".")
