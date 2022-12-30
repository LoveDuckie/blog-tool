from blog_tool.publishers.publisher_interface import PublisherInterface

import rich_click as click


class DevToPublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def upload(self, content: str):
        return super().upload(content)

    def extend_cli(self, cli_group: click.Group):
        return super().extend_cli(cli_group)
