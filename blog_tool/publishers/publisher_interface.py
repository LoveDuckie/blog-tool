from abc import ABC, abstractmethod


from blog_tool.models.blog import Blog


class PublisherInterface(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def publish(self, blog: Blog, **kwargs):
        """Publish the blog

        Args:
            blog (Blog): The blog instance

        Raises:
            ValueError: If the blog value is considered valid or not.
        """
        if blog is None:
            raise ValueError("The blog is invalid or null")
