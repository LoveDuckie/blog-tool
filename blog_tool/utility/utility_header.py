
from blog_tool.utility.paths.utility_paths import get_package_path
from blog_tool.utility.rich.utility_console import get_package_console
import os


def get_headers_path() -> str:
    """Generate the absolute path to where headers are sdtored

    Returns:
        str: The generated absolute path to where headers are stored
    """
    return get_package_path("data", "headers")


def get_header_filepath(header_filename: str) -> str:
    if not header_filename:
        raise ValueError("The header file name is invalid or null")
    return os.path.join(get_headers_path(), header_filename)


def echo_header(header_filename: str):
    if not header_filename:
        raise ValueError("The filename is invalid or null")
    package_console = get_package_console()
    header_filepath = get_header_filepath(header_filename)
    if not header_filepath:
        raise ValueError("The header filepath retrieved is invalid or null")

    if not os.path.exists(header_filepath):
        raise IOError(f"Failed: unable to find the file \"{header_filepath}\"")

    lines = None
    with open(header_filepath, "r") as file:
        lines = file.readlines
    for line in lines:
        package_console.print(f"[white]{line}[/white]")
