from blog_tool.models.blog import Blog
from blog_tool.publishers.publisher_interface import PublisherInterface
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport


def get_hashnode_api_url(*paths) -> str:
    """
    Get the API URL
    Args:
        *paths:

    Returns:

    """
    return f"https://api.hashnode.com/{'/'.join(paths)}"


class HashNodePublisher(PublisherInterface):
    """
    The publisher implemetnation
    """
    def __init__(self, *args, **kwargs) -> None:
        if 'hashnode_api_token' not in kwargs:
            raise KeyError("The Hashnode API token was not defined")
        self._api_token = kwargs['hashnode_api_token']
        transport_instance = AIOHTTPTransport(
            url=get_hashnode_api_url(), headers={"Authorization": self._api_token})

        client = Client(
            transport=transport_instance, fetch_schema_from_transport=True)
        self._client = client

        super().__init__(*args, **kwargs)

    async def publish(self, blog: Blog, **kwargs):
        if not blog:
            raise ValueError("The content is invalid or null")
        return super().publish(blog, **kwargs)
