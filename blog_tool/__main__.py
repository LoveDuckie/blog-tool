import sys
import os
from blog_tool.cli.cli_blogs import cli_blogs
from blog_tool.cli.cli_collections import cli_collections
from blog_tool.cli.cli_config import cli_config
from blog_tool.cli.cli_tests import cli_tests
from blog_tool.cli.cli_validate import cli_validate
from blog_tool.cli.cli_version import cli_version
from blog_tool.logging.blog_tool_logger import get_logger
import rich_click as click
from blog_tool.utility.utility_rich_click import click_console_echo_error, click_console_echo_exception


click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True

logger = get_logger()


@click.group(help="The command-line interface for the tool.")
@click.option("--path", "-p", "path", envvar="BLOG_TOOL_PATH",
              help="The path to where the blogs and collections are stored.", required=False, default=os.getcwd(),
              show_default=True)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


cli.add_command(cli_config)
cli.add_command(cli_tests)
cli.add_command(cli_collections)
cli.add_command(cli_blogs)
cli.add_command(cli_version)
cli.add_command(cli_validate)


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except Exception as exc:
        click_console_echo_error("An exception occurred.")
        click_console_echo_exception(exc)
