import datetime


def get_formatted_date() -> str:
    """Format the current timestamp into the string provided

    Returns:
        str: Returns the formatted timestamp
    """
    return datetime.datetime.now().strftime("%d-%m-%Y")


def get_formatted_datetime() -> str:
    """Format the current timestamp into the string provided

    Returns:
        str: Returns the formatted timestamp
    """
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def get_formatted_timestamp() -> str:
    """Generate a formatted timestamp

    Returns:
        str: The formatted timestamp to use
    """
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')
