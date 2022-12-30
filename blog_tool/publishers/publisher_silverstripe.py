from blog_tool.publishers.publisher_interface import PublisherInterface


class SilverstripePublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def upload(self, content: str):
        return super().export()
