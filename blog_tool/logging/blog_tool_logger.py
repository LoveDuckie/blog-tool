
import logging
import os
from rich.logging import RichHandler

from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler
from blog_tool import __title__
from blog_tool.utility.rich.utility_console import get_package_console
from blog_tool.utility.utility_datetime import get_formatted_timestamp
from blog_tool.utility.utility_names import sanitize_name

_logger_instance = None

loggers: dict[str, Logger] = None

_log_filename: str = None
_default_logs_path: str = None
_default_log_filepath: str = None


def get_default_log_filename() -> str:
    """Generate the default log file name to use

    Returns:
        str: The log filename to use for logging purpsoes
    """
    global _log_filename
    if not _log_filename:
        _log_filename = f"{sanitize_name(__title__)}_{get_formatted_timestamp()}.log"
    return _log_filename


def get_default_logs_path() -> str:
    """Get the absolute path to where the lots are stored on disk

    Returns:
        str: Returns the absolute path to where the logs are stored on disk
    """
    global _default_logs_path
    if not _default_logs_path:
        _default_logs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))
    return _default_logs_path


def get_default_log_filepath() -> str:
    """Get the absolute path to where the log is stored

    Returns:
        str: The absolute path to where the log is stored
    """
    global _default_log_filepath
    if not _default_log_filepath:
        _default_log_filepath = os.path.abspath(os.path.join(get_default_logs_path(), get_default_log_filename()))
    return _default_log_filepath


def _create_logger(logger_name: str = __title__) -> Logger:
    if logger_name is None:
        raise ValueError("The logger name specified is invalid or null")
    logger_instance = logging.getLogger(name='blog-tool-logger')

    if not os.path.exists(get_default_logs_path()):
        os.makedirs(get_default_logs_path())

    # FORMAT = "%(asctime)s | %(levelname)8s | %(message)s"
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="WARNING", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(console=get_package_console())]
    )
    logger_instance.addHandler(
        logging.handlers.RotatingFileHandler(get_default_log_filepath()))

    logger_instance.addHandler(StreamHandler())
    logger_instance.addHandler(
        RotatingFileHandler(get_default_log_filepath()))
    return logger_instance


def get_logger(logger_name: str = __title__):
    """Retrieve the logger used around the repository

    Args:
        logger_name (str, optional): The name of the logger. Defaults to __title__.

    Returns:
        str: The newly instantiated logger.
    """
    global _logger_instance

    if _logger_instance is None:
        _logger_instance = _create_logger(logger_name)

    return _logger_instance
