from blog_tool.image_uploaders.image_uploader_interface import ImageUploaderInterface


class ImageUploader:
    def __init__(self) -> None:
        pass

    def upload(self, uploader_interface: ImageUploaderInterface, **kwargs):
        if not uploader_interface:
            raise ValueError("The image uploader interface specified is invalid or null")

        try:
            if uploader_interface.requires_authentication():
                uploader_interface.authenticate(**kwargs)

            uploader_interface
        except Exception as exc:
            return
        return

