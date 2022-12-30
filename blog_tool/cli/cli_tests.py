import os
import rich_click as click
from blog_tool.utility.utility_tests import get_tests_path


@click.group("tests", help="Run unit tests.")
@click.option("--path", "-p", "path", type=str, default=get_tests_path(),
              help="The absolute path to where unit tests are defined.")
@click.pass_context
def cli_tests(ctx, path: str):
    ctx.ensure_object(dict)
    if ctx is None:
        raise ValueError("The context object is invalid or null")

    if not path:
        raise ValueError("The tests path is invalid or null")

    if not os.path.isabs(path):
        raise IOError(f"Failed: the path \"{path}\" is invalid.")

    if not os.path.exists(path):
        raise IOError(f"Failed: unable to find the tests \"{path}\".")


@cli_tests.command("run", help="Run all available tests.")
@click.pass_context
def cli_tests_run(ctx):
    ctx.ensure_object(dict)


@cli_tests.command("list", help="List all available tests that can be used")
@click.pass_context
def cli_tests_list(ctx):
    ctx.ensure_object(dict)
