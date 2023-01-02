import rich_click as click
from blog_tool.utility.blogs.utility_blogs import is_valid_collection
from blog_tool.utility.click.utility_click import click_write_error
from blog_tool.utility.paths.utility_paths_blog import get_default_collection_id


@click.group("validate", help="Validate the integrity of the the repository.")
@click.pass_context
def cli_validate(ctx):
    ctx.ensure_object(dict)
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_validate.command("collection", help="Show the current configuration values.")
@click.option("--collection-id", "-c", "collection_id", required=False, type=str, default=get_default_collection_id(),
              help="The name of the collection to reveal configuration information about")
@click.pass_context
def cli_validate_collection(ctx, collection_id: str):
    ctx.ensure_object(dict)
    if collection_id is not None and not is_valid_collection(collection_id):
        click_write_error(f"The collection \"{collection_id}\" is not valid.")


@cli_validate.command("blog", help="Validates a single blog post in a collection.")
@click.option("--collection-id", "-c", "collection_id", type=str, default=get_default_collection_id(),
              required=False, help="The name of the collection to reveal configuration information about")
@click.option("--blog-id", "-b", "blog_id", type=str,
              required=True, help="The name of the collection to reveal configuration information about")
@click.pass_context
def cli_validate_blog(ctx, blog_id: str, collection_id: str):
    ctx.ensure_object(dict)
    if collection_id is not None and not is_valid_collection(collection_id):
        click_write_error(f"The collection \"{collection_id}\" is not valid.")
