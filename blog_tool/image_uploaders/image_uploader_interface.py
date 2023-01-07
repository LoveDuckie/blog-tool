

from abc import ABC, abstractmethod
import os


class ImageUploaderInterface(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def requires_authentication(self):
        return

    @abstractmethod
    def authenticate(self):
        return

    @abstractmethod
    def upload(self, target_filepath: str):
        if not target_filepath:
            raise ValueError("The target filepath is invalid or null")

        if not os.path.exists(target_filepath):
            raise IOError(
                f"The filepath \"{target_filepath}\" does not exist.")
