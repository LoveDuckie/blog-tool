import base64
import os


def encode_image_as_base64(target_filepath: str) -> str:
    if not target_filepath:
        raise ValueError("The target filepath is invalid or null. Unable to continue.")

    if not os.path.isabs(target_filepath):
        raise IOError(f"The path \"{target_filepath}\" is not absolute. Unable to continue.")

    if not os.path.isfile(target_filepath):
        raise IOError(f"The path \"{target_filepath}\" is not a valid file path. Unable to continue.")

    if not os.path.exists(target_filepath):
        raise IOError(f"The file \"{target_filepath}\" does not exist.")

    with open(target_filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


def decode_base64_as_image(target_filepath: str) -> bytes:
    if not target_filepath:
        raise ValueError("The target filepath is invalid or null. Unable to continue.")

    if not os.path.isabs(target_filepath):
        raise IOError(f"The path \"{target_filepath}\" is not absolute. Unable to continue.")
    if not os.path.isfile(target_filepath):
        raise IOError(f"The path \"{target_filepath}\" is not a valid file path. Unable to continue.")

    if not os.path.exists(target_filepath):
        raise IOError(f"The file \"{target_filepath}\" does not exist.")

    with open(target_filepath, "rb") as image_file:
        image_bytes = base64.b64decode(image_file.read())

    return image_bytes
