from typing import List
import os
import traceback
import rich_click as click
from blog_tool.utility.blogs.utility_blogs import create_blog, get_blogs, is_valid_blog
from blog_tool.utility.click.utility_click import click_write_debug, click_write_error, click_write_info
from blog_tool.utility.utility_exporters import get_exporter_modules_names
from blog_tool.utility.utility_names import create_id_from_name
from blog_tool.utility.paths.utility_paths_blog import get_default_collection_id, get_default_collection_path, get_default_collections_path


@click.group("blogs", help="Manage blogs.")
@click.option("--collection-id", "-c", "collection_id", type=str, required=False, default=get_default_collection_id(),
              help="The ID of the blog collection.")
@click.pass_context
def cli_blogs(ctx, collection_id: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    ctx.obj['collection_id'] = collection_id


@cli_blogs.command("create", help="Create a new blog in a collection.")
@click.option("--blog-name", "-n", "blog_name", type=str, default=None, required=True, prompt_required=True,
              prompt="Blog Name", help="The name of the blog to create.")
@click.option("--blog-description", "-d", "blog_description", type=str, default=None, required=False,
              prompt_required=True, prompt="Blog Description", help="The description of the blog to create.")
@click.option("--tag", "-t", "blog_tags", type=str, multiple=True, default=[],
              required=False, prompt_required=False, prompt="Blog Tags", help="The associative tags with this blog.")
@click.pass_context
def cli_blogs_create(ctx, blog_id: str, blog_name: str, blog_description: str, blog_tags: List[str]):
    ctx.ensure_object(dict)
    if blog_id is None:
        raise ValueError(
            "The name of the blog is invalid or null. Unable to continue.")

    collection_id: str = ctx.obj['collection_id']
    if not collection_id:
        raise ValueError("The collection ID is invalid or null")

    blog_id: str = create_id_from_name(blog_id)
    click_write_info(f"Creating: \"{blog_id}\"")
    try:
        create_blog(blog_id, collection_id, name=blog_name,
                    description=blog_description, tags=blog_tags)
    except Exception as exc:
        tb = traceback.format_exc()
        click_write_error(tb)


@cli_blogs.command("delete", help="Delete an existing blog from a collection.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_delete(ctx, blog_id: str):
    ctx.ensure_object(dict)
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    collection_id = ctx.obj['collection_id']
    path = ctx.obj['path']

    if not is_valid_blog(blog_id, collection_id, collections_path):
        click_write_error(f"The blog \"{blog_id}\" is not valid.")


@cli_blogs.command("validate", help="Delete an existing blog from a collection.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_validate(ctx, blog_id: str):
    ctx.ensure_object(dict)
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    collection_id = ctx.obj['collection_id']

    if not is_valid_blog(blog_id, collection_id, collections_path):
        click_write_error(f"The blog \"{blog_id}\" is not valid.")


@cli_blogs.command("open", help="Open an existing blog from the collection specified.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The ID of the blog.")
@click.pass_context
def cli_blogs_create(ctx, blog_id: str):
    ctx.ensure_object(dict)
    if blog_id is None:
        raise ValueError("The blog ID specified is invalid or null")


@cli_blogs.command("list", help="List all blogs.")
@click.pass_context
def cli_blogs_list(ctx):
    ctx.ensure_object(dict)
    collection_id = ctx.obj['collection_id']
    path = ctx.obj['path']
    if not collection_id:
        raise ValueError("The collection ID is invalid or null")
    collections_path = get_default_collections_path(path)
    collection_path = get_default_collection_path()

    click_write_info(f"Listing Blogs: \"{collection_id}\"")
    click_write_debug(f"Collection Path: \"{collections_path}\"")

    blogs = get_blogs(collection_id, collections_path)

    if not blogs:
        raise ValueError("The blogs found are invalid or null")

    click_write_info(f"Blogs found in collection \"{collection_id}\"")

    for blog in blogs:
        click_write_info(f"Blog: \"{blog.name}\"")


@cli_blogs.command("info", help="Display information for a blog.")
@click.pass_context
def cli_blogs_list(ctx):
    collection_id = ctx.obj['collection_id']

    click_write_info(f"Listing Blogs: \"{collection_id}\"")
    click_write_debug(f"Collections Path: \"{collections_path}\"")

    blogs = get_blogs(collection_id, collections_path)

    if not blogs:
        raise ValueError("The blogs found are invalid or null")

    click_write_info(f"Blogs found in collection \"{collection_id}\"")

    for blog in blogs:
        click_write_info(f"Blog: \"{blog.name}\"")


@click.group("export", help="Render the blog out to a path specified.")
@click.option("--exporter", type=click.Choice(get_exporter_modules_names(),
                                              case_sensitive=True),
              multiple=True, required=True, help="The type qualification for the exporter to use.")
@click.option("--collections-path", "-p", "collections_path", default=get_default_collections_path(),
              required=False, help="The absolute path to where the collections are stored.")
@click.option("--collection-id", "-c", "collection_id", default=get_default_collection_id(),
              required=False, help="The ID or name of the collection to export the blog from.")
@click.option("--blog-id", "-b", "blog_id", required=True, help="Overwrite any exported blogs if they exist already.")
@click.option("--force", "-f", "force", is_flag=True, help="Overwrite any exported blogs if they exist already.")
@click.option("--output-path", "-o", "output_path", type=str, help="The output path for the exporter (where relevant).")
@click.pass_context
def cli_export(ctx, exporter: str, force: bool, output_path: str):
    ctx.ensure_object(dict)
    collection_id = ctx.obj['collection_id']
    blog_id = ctx.obj['blog_id']
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    if output_path is None:
        raise ValueError("The path is invalid or null")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if exporter is None:
        raise ValueError("The exporter type to use is invalid or null")
