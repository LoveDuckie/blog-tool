import os


def get_tool_environment_variables(prefix="BLOG_TOOL_") -> list:
    """Get environment variables for the tool

    Returns:
        list: A list of environment variables
    """
    return list(filter(lambda x: x[0].startswith(prefix), os.environ.items()))


def get_tool_environment_variables_as_dict() -> dict:
    if items := get_tool_environment_variables():
        return {item[0]: item[1] for item in items}
    else:
        raise ValueError("The environment variables are invalid or null")
