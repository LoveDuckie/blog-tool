import rich_click as click


@click.group("version", help="Display versioning information for this tool.")
@click.pass_context
def cli_version(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_version.command("show", help="Show the current configuration values.")
@click.pass_context
def cli_version_show(ctx):
    pass
