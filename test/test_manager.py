import os
from model.manager import comprobar_archivo_json, registro_valido

REGISTRO_VALIDO = {"fecha": "", "zona": "", "temperatura": "", "humedad": "", "viento": ""}
REGISTRO_INVALIDO = {"fechas": "", "zona": "", "temperatura": "", "humedad": "", "viento": ""}

def test_comprobar_archivo_json():
    assert comprobar_archivo_json() == os.path.join("data", "register.json")

def test_registro_valido():
    assert registro_valido(REGISTRO_VALIDO) is True

def test_registro_invalido():
    assert registro_valido(REGISTRO_INVALIDO) is False

def test_registro_vacio():
    assert registro_valido({}) is False  # caso mapa vacío