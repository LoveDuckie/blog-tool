import os
from typing import List
from blog_tool.models.blog_collection import BlogCollection
import rich_click as click
from blog_tool.utility.blogs.utility_blogs import create_collection, get_collections, is_valid_collection
from blog_tool.utility.click.utility_click import click_write_error, click_write_info, click_write_success
from blog_tool.utility.rich.utility_rich import get_panel
from blog_tool.utility.utility_names import create_id_from_name
from blog_tool.utility.paths.utility_paths_blog import get_default_collection_id, get_default_collections_path


@click.group("collections", help="Manage collections of blogs.")
@click.option("--collection-id", "-c", "collection_id", type=str, required=False, default=get_default_collection_id(),
              help="The ID of the blog collection.")
@click.option("--collection-path", "-p", "collections_path", type=str, required=False,
              default=get_default_collections_path(),
              help="The path to where the collections are stored.")
@click.pass_context
def cli_collections(ctx, collection_id: str, collections_path: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")

    ctx.obj['collection_id'] = collection_id

    storage_path = ctx.obj['storage_path']

    if not os.path.isabs(storage_path):
        raise IOError(f"The storage path \"{storage_path}\" is not an absolute path.")
    if not os.path.isdir(storage_path):
        raise IOError(f"The storage path \"{storage_path}\" is not a valid directory.")
    if not os.path.exists(storage_path):
        raise IOError(f"The storage path \"{storage_path}\" does not exist.")

    ctx.obj['collections_path'] = get_default_collections_path(storage_path)


@cli_collections.command("list", help="List all the collections.")
@click.option("--short", "-s", "short", is_flag=True, required=False,
              help="Display a shorter output from the list of collections.")
@click.pass_context
def cli_collection_list(ctx, short: bool):
    ctx.ensure_object(dict)
    collections_path = ctx.obj['collections_path']
    collections: list[BlogCollection] = get_collections(collections_path)
    panel_collections_path = get_panel("Collections Path", collections_path)
    panel_collections = get_panel("Collections", [collection.name for collection in collections])


@cli_collections.command("validate", help="Validate the collection and determine if there are any errors.")
def cli_collection_validate(ctx):
    ctx.ensure_object(dict)
    collections_path = ctx.obj['collections_path']
    collections: list[BlogCollection] = get_collections(collections_path)


@cli_collections.command("delete", help="Delete the collections specified.")
@click.option("--collection-id", "-c", "collection_ids", type=str, prompt="Collection ID", multiple=True, required=True,
              help="The slug ID(s) of he collection(s) to delete.")
@click.pass_context
def cli_collection_delete(ctx, collections: List[str]):
    if not collections:
        raise ValueError("The names specified are invalid or null")

    for collection in collections:
        continue


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
        click_write_error(
            f"The collection \"{name}\" already exists in \"{collections_path}\".")
        return 1

    click_write_info(f"Creating: \"{collection_id}\" in \"{collections_path}\"")
    collection = create_collection(
        collection_id, collections_path, description=description, name=name)
    if not collection:
        raise ValueError(
            f"Failed: unable to create the collection \"{collection_id}\" in \"{collections_path}\"")
    click_write_success("Done")
