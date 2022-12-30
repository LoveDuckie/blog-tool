
from blog_tool.utility.paths.utility_paths import get_package_path


def get_tests_path() -> str:
    return get_package_path("blog_tool", "tests")
