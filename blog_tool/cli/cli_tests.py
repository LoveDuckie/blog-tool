import os
import rich_click as click
from blog_tool.utility.utility_tests import get_tests_path


@click.group("tests", help="Run unit tests.")
@click.option("--tests-path", "-t", "tests_path", type=str, default=get_tests_path(),
              help="The absolute path to where unit tests are defined.")
@click.pass_context
def cli_tests(ctx, tests_path: str):
    ctx.ensure_object(dict)
    if ctx is None:
        raise ValueError("The context object is invalid or null")

    if not tests_path:
        raise ValueError("The tests path is invalid or null")

    if not os.path.isabs(tests_path):
        raise IOError(f"Failed: the path \"{tests_path}\" is invalid.")

    if not os.path.isdir(tests_path):
        raise IOError(f"Failed: the path \"{tests_path}\" is not a directory.")

    if not os.path.exists(tests_path):
        raise IOError(f"Failed: unable to find the tests \"{tests_path}\".")


@cli_tests.command("run", help="Run all available tests.")
@click.pass_context
def cli_tests_run(ctx):
    ctx.ensure_object(dict)


@cli_tests.command("list", help="List all available tests that can be used")
@click.pass_context
def cli_tests_list(ctx):
    ctx.ensure_object(dict)
