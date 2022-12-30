import rich_click as click
from blog_tool.utility.blogs.utility_blogs import is_valid_blog, is_valid_collection
from blog_tool.utility.click.utility_click import write_error
from blog_tool.utility.paths.utility_paths_blog import get_default_collections_path


@click.group("publish", help="Modify the behaviour of the blog_tool tool.")
@click.pass_context
def cli_publish(ctx):
    ctx.ensure_object(dict)
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_publish.command("blog", help="Publish a blog.")
@click.option("--blog-id", "-b", "blog_id", type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option("--collection-id", "-c", "collection_id", type=str, default="default", required=True, prompt=True, prompt_required=True)
@click.pass_context
def cli_publish_blog(ctx, blog_id: str, collection_id: str):
    ctx.ensure_object(dict)
    path = ctx.obj["path"] if "path" in ctx.obj else None
    if not path:
        raise ValueError("The root path to the blogs is invalid or null")
    collections_path = get_default_collections_path()
    if not blog_id:
        raise ValueError("The blog ID is invalid or null")
    if not collection_id:
        raise ValueError("The collect ID is invalid or null")
    if not collections_path:
        raise ValueError("The collections path is invalid or null")

    if not is_valid_collection(collection_id, collections_path):
        write_error(f"The collection \"{collection_id}\" is not valid.")
        ctx.exit(1)
    if not is_valid_blog(blog_id, collection_id, collections_path):
        write_error(f"The blog \"{blog_id}\" is not valid.")
        ctx.exit(2)
    ctx.exit(0)


@cli_publish.command("collection", help="Publish a collection.")
@click.option('--collection-id', '-c', 'collection_id', type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.pass_context
def cli_publish_collection(ctx, collection_id: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID specified is invalid or null")
