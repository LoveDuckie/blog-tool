from blog_tool.models.blog import Blog
from blog_tool.publishers.publisher_interface import PublisherInterface


class SilverstripePublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def publish(self, blog: Blog, **kwargs):
        if not blog:
            raise ValueError("The blog instance is invalid or null")
