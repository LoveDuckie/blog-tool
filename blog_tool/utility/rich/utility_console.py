from rich.console import Console
_console_instance: Console = None


def _create_console() -> Console:
    """Instantiate the console

    Returns:
        Console: The newly instantiated console
    """
    return Console()


def get_package_console() -> Console:
    """Retrieve the Rich Console instance with default settings applied

    Returns:
        Console: The "console" object with default settings applied.
    """
    global _console_instance
    if not _console_instance:
        _console_instance = _create_console()
    return _console_instance


def _format_messages(*msgs) -> str:
    return ' '.join(msgs) if msgs and any(msgs) else ''


def console_echo_warning(*msgs):
    get_package_console().print(f"[yellow]{_format_messages(*msgs)}[/yellow]")


def console_echo_success(*msgs):
    get_package_console().print(f"[green]{_format_messages(*msgs)}[/green]")


def console_echo(*msgs):
    get_package_console().print(_format_messages(*msgs))


def console_echo_error(*msgs):
    get_package_console().print(f"[red]{_format_messages(*msgs)}[/red]")


def console_echo_exception(exception: Exception, *msgs):
    if exception is None:
        raise ValueError("The excpetion is invalid or null")
    message = _format_messages(*msgs)
    get_package_console().print("")
