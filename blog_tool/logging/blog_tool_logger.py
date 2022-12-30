
import logging
import os
from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler

blog_tool_logger = None

loggers: dict[str, Logger] = None


def get_default_log_filename() -> str:
    return


def get_default_log_filepath() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))


def _create_logger(logger_name: str = 'blog_tool') -> Logger:
    if logger_name is None:
        raise ValueError("The logger name specified is invalid or null")
    blog_tool_logger = logging.getLogger(name='blog_tool-logger')
    blog_tool_logger.addHandler(StreamHandler())
    blog_tool_logger.addHandler(
        RotatingFileHandler(get_default_log_filepath()))
    return blog_tool_logger


def get_logger(logger_name: str = 'blog_tool'):
    global blog_tool_logger

    if blog_tool_logger is None:
        blog_tool_logger = _create_logger(logger_name)

    return blog_tool_logger
