from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from blog_tool.models.blog import Blog


class HashnodeInterface:
    def __init__(self, api_key: str, endpoint: str = None):
        """
        The constructor function
        Args:
            api_key: The API key used for interfacing with the API.
            endpoint: The API endpoint.Ï
        """
        if not endpoint:
            raise ValueError("The endpoint is invalid or null")

        if not api_key:
            raise ValueError("The API token specified is invalid or null")

        # Select your transport with a defined url endpoint
        transport = AIOHTTPTransport(url=f"{HashnodeInterface.get_hashnode_api_url()}",
                                     headers={"Authorization": api_key})

        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def __get_post(self, post_slug: str):
        pass

    def update_post(self, post_id: str):
        if not post_id:
            raise ValueError("The post ID specified is invalid or null")
        pass

    def create_post(self, blog: Blog):
        if not blog:
            raise ValueError("The blog specified is invalid or null")


        pass

    @staticmethod
    def get_hashnode_base_api_url(use_https: bool = True) -> str:
        """
        Get the base API URL to use
        Args:
            use_https: If the HTTPS protocol should be defined.

        Returns: The newly formed URL

        """
        protocol = "https" if use_https else "http"
        return f"{protocol}://api.hashnode.com"

    @staticmethod
    def get_hashnode_api_url(*paths) -> str:
        """
        Get the API URL to use.
        Args:
            *paths:

        Returns:

        """
        if paths is None:
            raise ValueError("The paths specified is invalid or null")
        combined = '/'.join(*paths)
        return f"{HashnodeInterface.get_hashnode_base_api_url()}/{combined}"
