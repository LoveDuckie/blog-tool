import os


def get_tool_environment_variable_name(name: str) -> str:
    """Return the environmnet variable name

    Args:
        name (str): The name of the environment variable to transform

    Returns:
        str: The environment variable name
    """
    return f"{get_default_tool_environment_prefix()}_{name.upper()}"


def get_default_tool_environment_prefix() -> str:
    """Get the environment prefix for the tool

    Returns:
        str: The environment prefix for the tool
    """
    return "BLOG_TOOL_"


def get_tool_environment_variables(prefix=get_default_tool_environment_prefix()) -> list:
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
