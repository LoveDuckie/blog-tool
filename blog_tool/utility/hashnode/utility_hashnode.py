from aiohttp import BasicAuth
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def get_gql_client(endpoint: str, api_token: str) -> Client:
    """
    Instantiate the GraphQL client to use
    Args:
        endpoint:

    Returns:

    """
    if not endpoint:
        raise ValueError("The endpoint is invalid or null")

    if not api_token:
        raise ValueError("The API token specified is invalid or null")

    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url=f"{get_hashnode_api_url()}",
                                 headers={"Authorization": api_token})

    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client


def get_hashnode_user_posts(client: Client, username: str) -> list:
    """
    Get a list of posts published by the user specified.
    Args:
        username: The username
        api_key:

    Returns:

    """
    if not username:
        raise ValueError("The username is invalid or null")

    query: gql = gql(
        """
        query getContinents {
          continents {
            code
            name
          }
        }
    """
    )
    return []

def create_hashnode_publication_story(client: Client, content: str, **kwargs):
    return

def update_hashnode_publication_story(client: Client):
    return

def get_hashnode_post(slug:str):
    return

