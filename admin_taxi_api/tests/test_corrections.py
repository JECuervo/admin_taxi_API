from ..methods import corrections


def test_clean_string():

    string1 = "(Holá)quitar DROP    Tablen ñ"

    string = corrections.clean_str(string1)

    assert string == "Holaquitar DROP Tablen ñ"

    string2 = """''*+~@<>/\\{}[]"""

    string = corrections.clean_str(string2)

    assert string == ""


def test_correct_placa():

    placa1 = "tjf 567"
    placa = corrections.correct_placa(placa1)

    assert placa == "TJF567"

    placa1 = "pfc-3214"
    placa = corrections.correct_placa(placa1)

    assert placa == "PFC3214"

    placa1 = "GIF -  45"
    placa = corrections.correct_placa(placa1)

    assert placa == "GIF45"


def test_correct_name():

    name1 = "CARLOS    giraldo. Gutíerrez"
    name = corrections.correct_name(name1)

    assert name == "Carlos Giraldo Gutierrez"


def test_correct_fecha():

    fecha = "03/01/2024"
    iso_fecha = corrections.correct_fecha(fecha)
    assert iso_fecha == "2024-01-03"

    fecha = "2024-3-12"
    iso_fecha = corrections.correct_fecha(fecha)
    assert iso_fecha == "2024-03-12"

    fecha = "casa"
    try:
        iso_fecha = corrections.correct_fecha(fecha)
        assert False
    except ValueError:
        assert True


def test_correct_cel():
    "the correct_cel function has not been programmed yet"
    assert False
