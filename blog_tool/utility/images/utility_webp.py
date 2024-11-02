from PIL import Image
import os


def convert_image_to_webp(image_filepath: str, output_path: str, **kwargs) -> str:
    """
    Covert the image file to webp for optimization purposes
    Args:
        image_filepath: The absolute path to the image that should be converted.
        output_path: The absolute path to where the newly converted image should be saved.

    Returns:
        The absolute path to the new generated image file.
    """
    if not image_filepath:
        raise ValueError("The image specified is invalid or null")

    if not output_path:
        raise ValueError("The output path was not defined")

    if not os.path.exists(image_filepath):
        raise ValueError("The image filepath specified is invalid")

    image_quality: int = kwargs['image_quality'] if 'image_quality' in kwargs else 100

    convert_image_instance = Image.open(image_filepath)
    convert_image_instance.convert('RGB')
    image_filename = os.path.basename(image_filepath)
    if not image_filename:
        raise ValueError("The image filename specified is invalid or null")

    image_filename_without_ext: str = os.path.splitext(image_filename)[0]
    if image_filename_without_ext is None:
        raise ValueError("The image specified is invalid or null")
    new_image_filepath = os.path.join(output_path, f'{image_filename_without_ext}.webp')
    convert_image_instance.save(new_image_filepath, format="webp", optimize=True, quality=image_quality)
    return new_image_filepath
