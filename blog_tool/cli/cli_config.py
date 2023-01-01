import rich_click as click

from blog_tool.utility.rich.utility_rich import echo_panel


@click.group("config", help="Display and modify the configuration for this tool.")
@click.pass_context
def cli_config(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_config.command("show", help="Show the current configuration values.")
@click.pass_context
def cli_config_show(ctx):
    ctx.ensure_object(dict)
    if not "config_filepath" in ctx.obj:
        raise KeyError(f"Failed: unable to find the key \"config_filepath\" in global context.")


@cli_config.command("set", help="Set the current configuration values.")
@click.option("--key", "-k", "key", type=str, default=None, required=True,
              help="The key for the configuration property.")
@click.option("--value", "-v", "value", type=str, default=None, required=True,
              help="The value for the configuration property.")
@click.pass_context
def cli_config_set(ctx, key: str, value: str):
    ctx.ensure_object(dict)


@cli_config.command("remove", help="Remove the current configuration values.")
@click.pass_context
def cli_config_remove(ctx):
    ctx.ensure_object(dict)
