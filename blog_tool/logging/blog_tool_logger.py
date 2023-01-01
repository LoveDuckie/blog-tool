
import logging
import os
from rich.logging import RichHandler

from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler
from blog_tool import __title__
from blog_tool.utility.rich.utility_console import get_package_console
from blog_tool.utility.utility_datetime import get_formatted_timestamp

_logger_instance = None

loggers: dict[str, Logger] = None


def get_default_log_filename() -> str:
    return f"{__title__}_{get_formatted_timestamp()}.log"


def get_default_logs_path() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))


def get_default_log_filepath() -> str:
    return os.path.abspath(os.path.join(get_default_logs_path(), get_default_log_filename()))


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
    global _logger_instance

    if _logger_instance is None:
        _logger_instance = _create_logger(logger_name)

    return _logger_instance
