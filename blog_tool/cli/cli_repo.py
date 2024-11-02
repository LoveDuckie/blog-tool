import rich_click as click


@click.group("repo", help="Manage the repository containing blog data.")
@click.option("--path", "-p", "path", type=str, default="",
              help="The absolute path to where the repository is located.")
@click.pass_context
def cli_repo(ctx):
    ctx.ensure_object(dict)
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_repo.command("init", help="Initialise the repository at the path specified.")
@click.pass_context
def cli_repo_init(ctx):
    ctx.ensure_object(dict)


@cli_repo.command("validate", help="Initialise the repository at the path specified.")
@click.pass_context
def cli_repo_validate(ctx):
    ctx.ensure_object(dict)


@cli_repo.group("list", help="Initialise the repository at the path specified.")
@click.pass_context
def cli_repo_list(ctx):
    ctx.ensure_object(dict)
    path = ctx.obj['path']


@cli_repo_list.command("blogs", help="List all blogs in a collection.")
@click.pass_context
def cli_repo_list_blogs(ctx):
    ctx.ensure_object(dict)

# List Collections


@cli_repo_list.command("collections", help="List all collections in a repository.")
@click.pass_context
def cli_repo_list_collections(ctx):
    ctx.ensure_object(dict)
