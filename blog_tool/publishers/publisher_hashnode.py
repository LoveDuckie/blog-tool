from blog_tool.publishers.publisher_interface import PublisherInterface
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport


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

    async def publish(self, content: str, **kwargs):
        if not content:
            raise ValueError("The content is invalid or null")
        return super().publish(content, **kwargs)
