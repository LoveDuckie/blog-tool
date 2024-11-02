import rich_click as click


@click.group("profiles", help="Manage profiles for publishing blogs.")
@click.pass_context
def cli_profiles(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_profiles.command("add", help="Add a new profile.")
@click.option("--name", "-n", "name", type=str, default=None, required=True, help="")
@click.pass_context
def cli_profiles_add(ctx, name: str):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_profiles.command("delete", help="Delete an existing profile.")
@click.option("--name", "-n", "name", type=str, default=None, required=True, help="")
@click.pass_context
def cli_profiles_delete(ctx, name: str):
    if ctx is None:
        raise ValueError("The context object is invalid or null")
