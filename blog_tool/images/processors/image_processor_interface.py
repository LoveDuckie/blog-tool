

class ImageProcessorInterface:
    """

    """
    def __init__(self) -> None:
        pass

    def process(self, path: str):
        if not path:
            raise ValueError("The path specified is invalid or null")
        return
