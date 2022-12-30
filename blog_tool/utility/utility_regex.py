import re


def get_host_from_url(url: str) -> str:
    """Retrieve the host from the URL specified

    Args:
        url (str): The URL to retrieve the host from

    Raises:
        ValueError: If the URL is not valid
        ValueError: If the match is not valid or if the hostname could not be found

    Returns:
        str: The host found from the URL
    """
    if not url:
        raise ValueError("The URL is invalid or null")
    match = re.match(
        "http(s)?\:\/\/(?P<Hostname>[^\/]+)(\/)?", url)

    if not match or 'Hostname' not in match.groupdict():
        raise ValueError("The host name was not found in the match")
    return match['Hostname']


def is_valid_url(url: str) -> bool:
    if not url:
        raise ValueError("The URL is invalid or null")
    match = re.match(
        "http(s)?\:\/\/(?P<Hostname>[^\/]+)(\/)?", url)
    return match is not None


def _version_parse_pattern() -> str:
    """The pattern used for parsing the version number

    Returns:
        str: The regular expression pattern used for parsing
    """
    return "^v?(?P<major>[0-9]+)\.(?P<minor>[0-9]+)(\.(?P<patch>[0-9]+))?$"


def is_valid_version(version: str) -> bool:
    """Determine if the Gitlab tag version is valid

    Args:
        version (str): The project version to verify

    Raises:
        ValueError: If the version string specified is invalid or null

    Returns:
        bool: If the version string specified is valid or not
    """
    if not version:
        raise ValueError("The version is invalid or null")
    match = re.search(
        _version_parse_pattern(), version)
    return match is not None


def get_version_information(version_value: str) -> tuple:
    """Get Gitlab project version information by parsing the versioning string

    Args:
        version (str): The version information

    Raises:
        ValueError: If the version string is not considered valid

    Returns:
        tuple: A tuple consisting of the major, minor and patch version number.
    """
    if not is_valid_version(version_value):
        raise ValueError("The version is invalid or null")
    match = re.search(
        _version_parse_pattern(), version_value)

    return match['major'], match['minor'], match['patch']
