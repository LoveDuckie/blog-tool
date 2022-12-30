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


click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True

logger = get_logger()


@click.group(help="The command-line interface for the Publisher tool.")
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.group("tests", help="Run any of the available unit tests.")
@click.pass_context
def cli_tests(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")





@cli_blogs.command("open", help="Open an existing blog from the collection specified.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_create(ctx, blog_id: str):
    if blog_id is None:
        raise ValueError("The blog ID specified is invalid or null")

    write_success("Done")


@cli_blogs.command("list", help="List all blogs.")
@click.pass_context
def cli_blogs_list(ctx):
    collection_id = ctx.obj['collection_id']
    collections_path = ctx.obj['collections_path']

    write_info(f"Listing Blogs: \"{collection_id}\"")
    write_debug(f"Collections Path: \"{collections_path}\"")

    blogs = get_blogs(collection_id, collections_path)

    if not blogs:
        raise ValueError("The blogs found are invalid or null")

    write_info(f"Blogs found in collection \"{collection_id}\"")

    for blog in blogs:
        write_info(f"Blog: \"{blog.name}\"")

    write_success("Done")


@cli.group("collections", help="Manage collections of blogs.")
@click.option("--collections-path", "-p", "collections_path", type=str, required=False,
              default=get_default_collections_path(),
              help="The absolute path to where collections are stored.")
@click.pass_context
def cli_collections(ctx, collections_path: str):
    ctx.ensure_object(dict)
    if not collections_path:
        raise ValueError("The path is invalid or null")

    ctx.obj['collections_path'] = collections_path


@cli_collections.command("fix", help="Fix the collection if there are any errors.")
@click.option("--collection-id", "-c", "collection_id", type=str, default=get_default_collection_name(),
              help="The ID for the collection")
@click.option("--all", "-a", "validate_all", is_flag=True, help="If all collections should be fixed.")
def cli_collections_validate(ctx, collection_id: str, validate_all: bool):
    collections_path = ctx.obj['collections_path']
    if not collections_path:
        raise ValueError(
            "The absolute path to the collections is invalid or null")

    if not os.path.exists(collections_path):
        raise ValueError("The collections path is invalid or null")

    if not collection_id:
        raise ValueError("The collection ID specified is invalid or null")

    write_success("Done")


@cli_collections.command("validate", help="Validate the collection and determine if there are any errors.")
@click.option("--collection-id", "-c", "collection_id", type=str, default=get_default_collection_name(),
              help="The ID for the collection")
@click.option("--all", "-a", "validate_all", is_flag=True, help="If all collections should be validated.")
def cli_collections_validate(ctx, collection_id: str, validate_all: bool):
    collections_path = ctx.obj['collections_path']
    if not collections_path:
        raise ValueError(
            "The absolute path to the collections is invalid or null")

    if not os.path.exists(collections_path):
        raise ValueError("The collections path is invalid or null")

    error_messages = []
    for collection in os.listdir(collections_path):
        return

    if any(error_messages):
        for msg in error_messages:
            write_error(msg)





@cli_collections.command("delete", help="Delete the collections specified.")
@click.option("--collection-id", "-c", "collection_ids", type=str, prompt="Collection ID", multiple=True, required=True,
              help="The slug ID(s) of he collection(s) to delete.")
@click.pass_context
def cli_collections_delete(ctx, collections: List[str]):
    if not collections:
        raise ValueError("The names specified are invalid or null")

    for collection in collections:
        continue

    write_success("Done")


@cli_collections.command("create", help="Create a new collection of blogs.")
@click.option("--name", "-n", "name", required=True, prompt="Name of the collcetion", prompt_required=True,
              help="The name(s) of the collection to create.")
@click.option("--description", "-d", "description", required=False, prompt="Description of the collection",
              help="The useful description of the collection.")
@click.pass_context
def cli_collections_create(ctx, name: str, description: str):
    if name is None:
        raise ValueError("The name is invalid or null")

    if 'collections_path' not in ctx.obj:
        raise KeyError("Failed: unable to find the path to collections")

    collections_path = ctx.obj['collections_path']

    if collections_path is None:
        raise ValueError(
            "The collections path is invalid or null. Unable to continue.")

    if not os.path.exists(collections_path):
        raise IOError(
            f"Failed: unable to find the path \"{collections_path}\"")

    collection_id = create_id_from_name(name)

    if is_valid_collection(collection_id, collections_path):
        write_error(
            f"The collection \"{name}\" already exists in \"{collections_path}\".")
        return 1

    write_info(f"Creating: \"{collection_id}\" in \"{collections_path}\"")
    collection = create_collection(
        collection_id, collections_path, description=description, name=name)
    if not collection:
        raise ValueError(
            f"Failed: unable to create the collection \"{collection_id}\" in \"{collections_path}\"")
    write_success("Done")


@cli_config.command("blog_tool")
@click.option("--set", '-s', "parameters", type=str, required=True, prompt_required=True,
              help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_blog_tool(parameters: List[str]):
    for parameter in parameters:
        write_info(parameter)
    write_success("Done")


@cli_config.command("exporter")
@click.option("--type", "-t", type=str, help="The absolute type path for the exporter.")
@click.option("--parameter", '-p', "parameters", type=str, required=True, prompt_required=True,
              help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_exporter(parameters: List[str]):
    for parameter in parameters:
        write_info(parameter)
    write_success("Done")


@cli_config.command("uploader")
@click.option("--type", "-t", type=str, help="The type name")
@click.option("--parameter", '-p', "parameters", type=str, required=True, prompt_required=True, prompt="Parameter",
              default=[],
              help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_exporter(parameters: List[str]):
    if parameters is None:
        raise ValueError("The parameters are invalid or null.")
    if not any(parameters):
        raise ValueError("No parameters were found.")


@cli.group("upload", help="Upload a collection of blogs or a single blog.")
@click.pass_context
def cli_upload(ctx):
    ctx.ensure_object(dict)
    return


@cli_upload.command("blog", help="Upload a blog.")
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


@cli_upload.command("collection", help="Upload a collection.")
@click.option('--collection-id', '-c', 'collection_id', type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option('--collections-path', '-p', 'collections_path', type=str, default=get_default_collections_path(),
              required=False, prompt=True, prompt_required=True)
@click.pass_context
def cli_upload_collection(ctx, collection_id: str, collections_path: str):
    if collections_path is None:
        raise ValueError("The collections path specified is invalid or null")
    if collection_id is None:
        raise ValueError("The collection ID specified is invalid or null")


@cli.group("export", help="Render the blog out to a path specified.")
@click.option("--exporter", type=click.Choice(get_exporter_modules_names(),
                                              case_sensitive=True),
              multiple=True, required=True, help="The type qualification for the exporter to use.")
@click.option("--collections-path", "-p", "collections_path", default=get_default_collections_path(),
              required=False, help="The absolute path to where the collections are stored.")
@click.option("--collection-id", "-c", "collection_id", default=get_default_collection_name(),
              required=False, help="The ID or name of the collection to export the blog from.")
@click.option("--blog-id", "-b", "blog_id", required=True, help="Overwrite any exported blogs if they exist already.")
@click.option("--force", "-f", "force", is_flag=True, help="Overwrite any exported blogs if they exist already.")
@click.option("--output-path", "-o", "output_path", type=str, help="The output path for the exporter (where relevant).")
@click.pass_context
def cli_export(ctx, exporter: str, collections_path: str, collection_id: str, blog_id: str, force: bool, output_path: str):
    ctx.ensure_object(dict)

    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")
    if output_path is None:
        raise ValueError("The path is invalid or null")
    if exporter is None:
        raise ValueError("The exporter type to use is invalid or null")


if __name__ == "__main__":
    sys.exit(cli())
