import rich_click as click


@click.group("profiles", help="Manage profiles for publishing blogs.")
@click.pass_context
def cli_config(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")
