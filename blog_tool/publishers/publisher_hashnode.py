from blog_tool.publishers.publisher_interface import PublisherInterface
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
import rich_click as click

from blog_tool.utility.click.utility_click import click_write_success


def _cli_command_get_blogs(ctx):
    pass


def get_hashnode_api_url(*paths) -> str:
    return f"https://api.hashnode.com/{'/'.join(paths)}"


class HashNodePublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        if 'hashnode_api_token' not in kwargs:
            raise KeyError("The Hashnode API token was not defined")
        self._api_token = kwargs['hashnode_api_token']
        TRANSPORT = AIOHTTPTransport(
            url=get_hashnode_api_url(), headers={"Authorization": self._api_token})

        client = Client(
            transport=TRANSPORT, fetch_schema_from_transport=True)
        self._client = client

        super().__init__(*args, **kwargs)

    async def upload(self, content: str, **kwargs):
        return super().upload(content, **kwargs)

    def extend_cli(self, cli_group: click.Group):
        cli_group.add_command(_cli_command_get_blogs)
        return super().extend_cli(cli_group)
