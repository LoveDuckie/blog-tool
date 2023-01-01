import rich_click as click


def click_write_info(msg, *fmt):
    click.echo(click.style(msg, fg='white'))


def click_write_debug(msg, *fmt):
    click.echo(click.style(msg, fg='white'))


def click_write_error(msg, *fmt):
    click.echo(click.style(msg, fg='red'))


def click_write_success(msg, *fmt):
    click.echo(click.style(msg, fg='green'))


def click_write_critical(msg, *fmt):
    click.echo(click.style(msg, bold=True, blink=True, bg='red', fg='white'))


def click_write_warning(msg, *fmt):
    click.echo(click.style(msg, fg='yellow'))
