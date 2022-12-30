import os
from blog_tool.image_uploaders.image_uploader_interface import ImageUploaderInterface
from blog_tool.utility.utility_config import get_config_property

import rich_click as click


class ImgurImageUploader(ImageUploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        client_id = kwargs['client_id'] if 'client_id' in kwargs else get_config_property(
            "blog_tool.image-uploader.imgur", "client-id")
        client_secret = kwargs['client_secret'] if 'client_secret' in kwargs else get_config_property(
            "blog_tool.image-uploader.imgur", "client-secret")

    def requires_authentication(self) -> bool:
        return True

    def authenticate(self):
        return super().authenticate()

    def upload(self, target_filepath: str):
        super().upload(target_filepath)
