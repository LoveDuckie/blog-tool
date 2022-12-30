import traceback
import rich_click as click


def _format_messages(*msgs) -> str:
    return ' '.join(msgs) if msgs and any(msgs) else ''


def click_console_echo_warning(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='yellow'))


def click_console_echo(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='white'))


def click_console_echo_info(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='blue'))


def click_console_echo_success(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='green'))


def click_console_echo_error(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='red'))


def click_console_echo_failed(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='red'))


def click_console_echo_critical(*msgs):
    click.echo(click.style(_format_messages(*msgs), fg='red'))


def click_console_echo_exception(exception: Exception):
    """Format and output the contents of the exception

    Args:
        exception (Exception): _description_
    """
    formatted: list = traceback.format_exception(exception)
    formatted_concat = '\n'.join(formatted)
    click.echo(click.style(_format_messages(formatted_concat), fg='red'))
