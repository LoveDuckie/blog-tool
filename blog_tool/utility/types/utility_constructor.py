
import typing


def _init_parameter(obj, parameter: str, parameters: dict, required: bool = False):
    """Initialise the parameter if it exists in the dictionary of parameters (typically **kwargs)

    Args:
        obj (Any): Python class instance
        parameter (str): The name of the parameter
        parameters (dict): The kwargs container of parameters
        required (bool, optional): If the parameter is required. Throw if not found. Defaults to False.

    Raises:
        ValueError: If the object is invalid or null
        ValueError: If the parameter is invalid or null
        KeyError: If the parameter is not found in the kwargs
    """
    if obj is None:
        raise ValueError("The object is invalid or null")

    if parameter is None:
        raise ValueError("The parameter name is invalid or null")

    if parameter not in parameters:
        raise KeyError(f"Failed to find the parameter {parameter}.")

    setattr(obj, parameter, parameters[parameter])
