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
from blog_tool.utility.paths.utility_paths import get_default_user_config_filepath
from blog_tool.utility.rich.utility_rich import echo_panel_warning
from blog_tool.utility.utility_header import echo_header, get_default_header_name
from blog_tool.utility.utility_rich_click import click_console_echo_error, click_console_echo_exception
from blog_tool.utility.utility_variables import get_tool_environment_variable_name

click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True

logger = get_logger()

echo_header(get_default_header_name())


@click.group(help="The command-line interface for the tool.")
@click.option("--show-header", "-s", "show_header", envvar=get_tool_environment_variable_name("SHOW_HEADER"),
              is_flag=True, default=True, help="Display the ASCII header.")
@click.option("--storage-path", "-p", "storage_path", envvar=get_tool_environment_variable_name("STORAGE_PATH"),
              help="The path to where the blogs and collections are stored.", required=False, default=os.getcwd(),
              show_default=True)
@click.option("--create-storage-path", "-f", "create_storage_path",
              envvar=get_tool_environment_variable_name("CREATE_STORAGE_PATH"),
              help="Attempt to create the storage path for the blogs automatically.", required=False, default=True,
              show_default=True)
@click.option("--config-filepath", "-c", "config_filepath",
              envvar=get_tool_environment_variable_name("CONFIG_FILEPATH"),
              help="The absolute filepath to the configuration file.", required=False,
              default=get_default_user_config_filepath(),
              show_default=True)
@click.pass_context
def cli(ctx, storage_path: str, show_header: bool, config_filepath: str, create_storage_path: bool):
    """
    :param ctx: The Click context object, used to pass information between commands.
    :param storage_path: The path where blogs and collections are stored.
    :param show_header: Whether to display the ASCII header.
    :param config_filepath: The absolute file path to the configuration file.
    :param create_storage_path: Attempt to create the storage path for the blogs automatically if it does not exist.
    :return: None
    """
    ctx.ensure_object(dict)

    if not storage_path:
        raise ValueError("The storage path is invalid or null")
    if not os.path.isabs(storage_path):
        raise IOError("The storage path is not absolute")
    if not os.path.isdir(storage_path):
        raise IOError("The storage path is not a directory")

    if not os.path.exists(storage_path) and create_storage_path:
        echo_panel_warning("Invalid Storage Path", f"Creating storage path as it does not exist (\"{storage_path}\")")
        try:
            os.makedirs(storage_path)
        except IOError:
            return
    ctx.obj['storage_path'] = storage_path

    if not config_filepath:
        raise ValueError("The configuration file path is invalid or null")
    if not os.path.isabs(config_filepath):
        raise IOError("The configuration file path is not absolute")
    print(config_filepath)
    if not os.path.isfile(config_filepath):
        raise IOError("The configuration file path is not a valid file")
    if not os.path.exists(config_filepath):
        raise IOError("The configuration file path is invalid or null")
    ctx.obj['config_filepath'] = config_filepath


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
