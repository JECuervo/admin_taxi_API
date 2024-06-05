"""
module that corrects and formats api inputs
"""

import datetime
import re
from unicodedata import normalize


def clean_str(string: str) -> str:
    """
    clears the string of special characters and spaces at the beginning and end of the string

    Args:
        string (str): string

    Returns:
        str: clean_string
    """
    string_convert = string.replace("ñ", ".#.").replace("Ñ", ".%.")
    new_string = (
        normalize("NFKD", string_convert.strip())
        .encode("ascii", "ignore")
        .decode("ascii")
        .replace(".#.", "ñ")
        .replace(".%.", "Ñ")
    )
    new_string = re.sub(r"[^a-zA-Z0-9\sñ]", "", new_string)
    new_string = re.sub(r"\s+", " ", new_string)
    return new_string


def correct_name(name: str) -> str:
    """
    Clean string name and format title

    Args:
        name (str): string name

    Returns:
        str: correct name
    """
    name = clean_str(name)

    return name.title()


def correct_cel(cel: int) -> int:
    """
    pass function

    Args:
        cel (int): cel

    Returns:
        int: cel
    """
    return cel


def correct_placa(placa: str) -> str:
    """
    Clean string and return format

    XXXDDR

    Args:
        placa (str): string

    Returns:
        str: string
    """
    placa = clean_str(placa)
    placa = re.sub(r"\s", "", placa.upper())
    return placa


def correct_fecha(date: int | str) -> str:
    """
    Convert date to format iso

    Args:
        date (int | str): date in format %d/%m/%Y or time

    Returns:
        str: iso format date
    """
    if isinstance(date, str):
        try:
            date = datetime.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")

        return date.date().isoformat()

    date = datetime.date(date)
    return date.isoformat()
