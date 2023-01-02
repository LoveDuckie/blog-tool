from blog_tool.models.blog import Blog
from blog_tool.publishers.publisher_interface import PublisherInterface
import rich_click as click


def get_medium_api_url(*urls) -> str:
    urls_combined: str = '/'.join(urls)
    return f"https://api.medium.com/v1/{urls_combined}"


class MediumPublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def publish(self, blog: Blog, **kwargs):
        if not blog:
            raise ValueError("The content is invalid or null")
        return super().publish()
