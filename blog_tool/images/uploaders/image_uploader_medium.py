from blog_tool import __title__
from blog_tool.images.uploaders.image_uploader_interface import ImageUploaderInterface
from blog_tool.utility.config.utility_config import get_config_property


class MediumImageUploader(ImageUploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        client_id = kwargs['client_id'] if 'client_id' in kwargs else get_config_property(
            f"{__title__}.image-uploader.imgur", "client-id")
        client_secret = kwargs['client_secret'] if 'client_secret' in kwargs else get_config_property(
            f"{__title__}.image-uploader.imgur", "client-secret")
