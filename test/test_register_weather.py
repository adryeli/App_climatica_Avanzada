# test/test_test_register_weather.py
from unittest.mock import patch
from model.register_weather import (
    guardar_registro,
    obtener_registros,
    buscar_por_fecha,
    buscar_por_zona,
    eliminar_registros,
)

# Datos de ejemplo reutilizables

REGISTRO_VALIDO = {"fecha": "15-01-2026", "zona": "Madrid", "temperatura": 12}
REGISTRO_2      = {"fecha": "16-01-2026", "zona": "Barcelona", "temperatura": 18}
REGISTROS_MOCK  = [REGISTRO_VALIDO, REGISTRO_2]

# guardar_registro

@patch("model.register_weather.escribir_json")
@patch("model.register_weather.leer_json", return_value=[])
@patch("model.register_weather.registro_valido", return_value=True)
def test_guardar_registro_valido(mock_valido, mock_leer, mock_escribir):
    resultado = guardar_registro(REGISTRO_VALIDO)

    assert resultado is True
    mock_escribir.assert_called_once_with([REGISTRO_VALIDO])  # se guardó correctamente


@patch("model.register_weather.registro_valido", return_value=False)
def test_guardar_registro_invalido(mock_valido):
    resultado = guardar_registro({"datos": "incorrectos"})

    assert resultado is False  # rechaza el registro inválido


# obtener_registros

@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_obtener_registros(mock_leer):
    resultado = obtener_registros()

    assert resultado == REGISTROS_MOCK
    assert len(resultado) == 2


@patch("model.register_weather.leer_json", return_value=[])
def test_obtener_registros_vacio(mock_leer):
    assert obtener_registros() == []


# buscar_por_fecha

@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_buscar_por_fecha_encontrado(mock_leer):
    resultado = buscar_por_fecha("15-01-2026")

    assert len(resultado) == 1
    assert resultado[0]["zona"] == "Madrid"


@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_buscar_por_fecha_no_encontrado(mock_leer):
    resultado = buscar_por_fecha("1999-01-01")

    assert resultado == []


# buscar_por_zona

@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_buscar_por_zona_encontrado(mock_leer):
    resultado = buscar_por_zona("madrid")  # minúsculas a propósito

    assert len(resultado) == 1
    assert resultado[0]["temperatura"] == 12


@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_buscar_por_zona_case_insensitive(mock_leer):
    resultado = buscar_por_zona("BARCELONA")  # mayúsculas a //

    assert len(resultado) == 1
    assert resultado[0]["fecha"] == "16-01-2026"


@patch("model.register_weather.leer_json", return_value=REGISTROS_MOCK)
def test_buscar_por_zona_no_encontrado(mock_leer):
    assert buscar_por_zona("Valencia") == []


# eliminar_registros

@patch("model.register_weather.escribir_json")
def test_eliminar_registros(mock_escribir):
    resultado = eliminar_registros()

    assert resultado is True
    mock_escribir.assert_called_once_with([])  # se llamó con lista vacía