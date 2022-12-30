from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn
from rich import print

from blog_tool.logging.utils.utils_rich_console import get_package_console


def get_progress_bar() -> Progress:
    return Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=get_package_console(),
        transient=False, expand=True)


def get_panel_success(title: str, message: str | list[str]) -> Panel:
    if message is None:
        raise ValueError("The message specified is invalid or null")
    if not isinstance(message, str) and not isinstance(message, list):
        raise TypeError("The expected type should be list of strings, or a string.")
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    if not title:
        raise ValueError("The title specified is invalid or null")
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]{title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="green")
    console_panel.style = Style(blink=False, color="green")
    return console_panel


def get_panel_error(title: str, message: str | list[str]) -> Panel:
    if message is None:
        raise ValueError("The message specified is invalid or null")
    if not isinstance(message, str) and not isinstance(message, list):
        raise TypeError("The expected type should be list of strings, or a string.")
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    if not title:
        raise ValueError("The title specified is invalid or null")
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]{title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="red")
    console_panel.style = Style(blink=False, color="red")
    return console_panel


def get_panel_warning(title: str, message: str | list[str]) -> Panel:
    if message is None:
        raise ValueError("The message specified is invalid or null")
    if not isinstance(message, str) and not isinstance(message, list):
        raise TypeError("The expected type should be list of strings, or a string.")
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    if not title:
        raise ValueError("The title specified is invalid or null")
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]{title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="yellow")
    console_panel.style = Style(blink=False, color="yellow")
    return console_panel


def get_panel(title: str, message: str | list[str]) -> Panel:
    if not isinstance(message, str) and not isinstance(message, list):
        raise TypeError("The expected type should be list of strings, or a string.")
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]{title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="white")
    console_panel.style = Style(blink=False, color="white")
    return console_panel


def echo_panel_warning(title: str, message: str | list[str]):
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]:warning: {title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="yellow")
    console_panel.style = Style(blink=False, color="yellow")
    get_package_console().print(console_panel)


def echo_panel_success(title: str, message: str | list[str]):
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]:white_check_mark: {title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="green")
    console_panel.style = Style(blink=False, color="green")
    get_package_console().print(console_panel)


def echo_panel_error(title: str, message: str | list[str]):
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]:x: {title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="red")
    console_panel.style = Style(blink=False, color="red")
    get_package_console().print(console_panel)


def echo_panel_fatal(title: str, message: str | list[str]):
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel: Panel = Panel(panel_message,
                                 title=f"[b]:x: {title}[/b]")
    console_panel.border = "encircle"
    console_panel.border_style = Style(blink=False, color="red")
    console_panel.style = Style(blink=False, color="red")
    get_package_console().print(console_panel)


def echo_panel(title: str, message: str | list[str]):
    panel_message = message if isinstance(message, str) else '\r\n'.join(message)
    console_panel = get_panel(title, panel_message)
    get_package_console().print(console_panel)


def echo_table_dictionary(title: str, data: dict):
    if not data:
        raise ValueError("The data is invalid or null")
    if not title:
        raise ValueError("The title is invalid or null")
    table: Table = Table(title=title, title_justify="center")
    table.add_column("Property")
    table.add_column("Value")
    table.expand = True
    for key, value in data.items():
        table.add_row(key, value)
    get_package_console().print(table)
