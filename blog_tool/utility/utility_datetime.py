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
