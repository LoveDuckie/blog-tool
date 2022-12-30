from blog_tool.utility.paths.utility_paths import get_package_path


def get_tests_path() -> str:
    """Generate the absolute path to where the tests are stored

    Returns:
        str: The absolute path to where the tests are stored on disk.
    """
    return get_package_path("blog_tool", "tests")
