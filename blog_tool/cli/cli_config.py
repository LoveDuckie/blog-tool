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


@click.group("config", help="Modify the behaviour of the blog_tool tool.")
@click.pass_context
def cli_config(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_config.command("show", help="Show the current configuration values.")
@click.pass_context
def cli_config_show(ctx):
    pass


@cli_config.command("set", help="Set the current configuration values.")
@click.pass_context
def cli_config_set(ctx):
    pass


@cli_config.command("remove", help="Remove the current configuration values.")
@click.pass_context
def cli_config_remove(ctx):
    pass
