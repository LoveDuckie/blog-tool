import rich_click as click


@click.group("config", help="Display and modify the configuration for this tool.")
@click.pass_context
def cli_config(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_config.command("show", help="Show the current configuration values.")
@click.pass_context
def cli_config_show(ctx):
    ctx.ensure_object(dict)


@cli_config.command("set", help="Set the current configuration values.")
@click.pass_context
def cli_config_set(ctx):
    ctx.ensure_object(dict)


@cli_config.command("remove", help="Remove the current configuration values.")
@click.pass_context
def cli_config_remove(ctx):
    ctx.ensure_object(dict)
