"""
module to validate API entries
"""

import re
from datetime import datetime
from .exceptions import APIValidationError


def validate_name(name: str) -> bool:
    """
    Validate inputs name

    Args:
        name (str): name value

    Raises:
        APIValidationError: invalid type
        APIValidationError: void value
        APIValidationError: max length 50

    Returns:
        bool: False if no raise
    """
    if not isinstance(name, str):
        raise APIValidationError("No valid type value")
    if not name:
        raise APIValidationError("empty name")
    if len(name) > 50:
        raise APIValidationError(f"max name len 50: len name {len(name)}")

    return False


def validate_placa(placa: str) -> bool:
    """
    Validate placas

    format: XXXDDR
    X: Letter
    D: digit
    R: letter,digit,void

    Args:
        placa (str): placa str

    Raises:
        APIValidationError: if no format valid

    Returns:
        bool: False if no raise
    """
    result = re.match(r"^[A-Z]{3}[0-9]{2}([0-9A-Z])*\z", placa)

    if not result:
        raise APIValidationError(
            "placa no format correct XXXDDR with X letter D digit R digit,letter o none"
        )

    return False


def validate_cel(cel: int) -> bool:
    """
    validate cell phone numbers

    Args:
        cel (int): num cel

    Raises:
        APIValidationError: if length diff 10
        APIValidationError: if first value diff 3

    Returns:
        bool: False if no raise
    """
    cel = str(cel)

    if len(cel) != 10:
        raise APIValidationError("len cel error diff 10")
    if cel[0] != "3":
        raise APIValidationError("No valid format number cel")

    return False


def validate_fecha(fecha: str) -> bool:
    """
    Validate format iso date:
    YYYY-MM-DD

    Args:
        fecha (str): iso date

    Raises:
        APIValidationError: if no format valid

    Returns:
        bool: false if no raise
    """
    try:
        datetime.strptime(fecha, "%Y-%m-%d")

    except ValueError as error:
        raise APIValidationError("no format valid") from error

    return False
