from datetime import datetime
from controller.control_time import (
    validar_fecha,
    validar_zona,
    validar_temperatura,
    validar_humedad,
    validar_viento,
    validar_registro_climatico,
)

ZONAS = {"1": "Centro", "2": "Norte", "3": "Sur", "4": "Este", "5": "Oeste"}


# validar_fecha

def test_fecha_valida():
    ok, resultado = validar_fecha("01-01-2025")
    assert ok is True
    assert resultado == "01-01-2025"

def test_fecha_futura():
    ok, msg = validar_fecha("01-01-2099")
    assert ok is False
    assert "futura" in msg

def test_fecha_muy_antigua():
    ok, msg = validar_fecha("01-01-1900")
    assert ok is False
    assert "10 años" in msg

def test_fecha_formato_invalido():
    ok, msg = validar_fecha("2025/01/01")
    assert ok is False
    assert "formato" in msg.lower()

def test_fecha_texto():
    ok, msg = validar_fecha("hola")
    assert ok is False

def test_fecha_vacia():
    ok, msg = validar_fecha("")
    assert ok is False

def test_fecha_none():
    ok, msg = validar_fecha(None)
    assert ok is False

def test_fecha_hoy():
    hoy = datetime.now().strftime("%d-%m-%Y")
    ok, resultado = validar_fecha(hoy)
    assert ok is True
    assert resultado == hoy


# validar_zona

def test_zona_valida():
    ok, resultado = validar_zona("1", ZONAS)
    assert ok is True
    assert resultado == "1"

def test_zona_invalida():
    ok, msg = validar_zona("9", ZONAS)
    assert ok is False
    assert "inválida" in msg.lower()

def test_zona_vacia():
    ok, msg = validar_zona("", ZONAS)
    assert ok is False
    assert "vacía" in msg.lower()

def test_zona_espacios():
    ok, resultado = validar_zona("  2  ", ZONAS)
    assert ok is True
    assert resultado == "2"

def test_zona_no_string():
    ok, msg = validar_zona(2, ZONAS)
    assert ok is False

def test_zona_none():
    ok, msg = validar_zona(None, ZONAS)
    assert ok is False


# validar_temperatura

def test_temperatura_valida():
    ok, resultado = validar_temperatura(25)
    assert ok is True
    assert resultado == 25.0

def test_temperatura_limite_superior():
    ok, resultado = validar_temperatura(50)
    assert ok is True

def test_temperatura_limite_inferior():
    ok, resultado = validar_temperatura(-20)
    assert ok is True

def test_temperatura_fuera_rango_alto():
    ok, msg = validar_temperatura(51)
    assert ok is False
    assert "50" in msg

def test_temperatura_fuera_rango_bajo():
    ok, msg = validar_temperatura(-21)
    assert ok is False
    assert "-20" in msg

def test_temperatura_string_numero():
    ok, resultado = validar_temperatura("33")
    assert ok is True
    assert resultado == 33.0

def test_temperatura_texto():
    ok, msg = validar_temperatura("mucho calor")
    assert ok is False

def test_temperatura_none():
    ok, msg = validar_temperatura(None)
    assert ok is False


# validar_humedad

def test_humedad_valida():
    ok, resultado = validar_humedad(60)
    assert ok is True
    assert resultado == 60.0

def test_humedad_limite_inferior():
    ok, resultado = validar_humedad(0)
    assert ok is True

def test_humedad_limite_superior():
    ok, resultado = validar_humedad(100)
    assert ok is True

def test_humedad_negativa():
    ok, msg = validar_humedad(-1)
    assert ok is False

def test_humedad_mayor_100():
    ok, msg = validar_humedad(101)
    assert ok is False

def test_humedad_texto():
    ok, msg = validar_humedad("mucha")
    assert ok is False

def test_humedad_none():
    ok, msg = validar_humedad(None)
    assert ok is False


# validar_viento

def test_viento_valido():
    ok, resultado = validar_viento(80)
    assert ok is True
    assert resultado == 80.0

def test_viento_cero():
    ok, resultado = validar_viento(0)
    assert ok is True

def test_viento_limite_superior():
    ok, resultado = validar_viento(500)
    assert ok is True

def test_viento_negativo():
    ok, msg = validar_viento(-1)
    assert ok is False
    assert "negativa" in msg.lower()

def test_viento_mayor_500():
    ok, msg = validar_viento(501)
    assert ok is False
    assert "500" in msg

def test_viento_texto():
    ok, msg = validar_viento("fuerte")
    assert ok is False

def test_viento_none():
    ok, msg = validar_viento(None)
    assert ok is False


# validar_registro_climatico

def test_registro_valido_completo():
    hoy = datetime.now().strftime("%d-%m-%Y")
    ok, resultado = validar_registro_climatico(hoy, "1", "25", "60", "30", ZONAS)
    assert ok is True
    assert resultado["zona"] == "1"
    assert resultado["temperatura"] == 25.0
    assert resultado["humedad"] == 60.0
    assert resultado["viento"] == 30.0

def test_registro_con_error_fecha():
    ok, errores = validar_registro_climatico("99-99-9999", "1", "25", "60", "30", ZONAS)
    assert ok is False
    assert "fecha" in errores

def test_registro_con_error_zona():
    hoy = datetime.now().strftime("%d-%m-%Y")
    ok, errores = validar_registro_climatico(hoy, "9", "25", "60", "30", ZONAS)
    assert ok is False
    assert "zona" in errores

def test_registro_con_error_temperatura():
    hoy = datetime.now().strftime("%d-%m-%Y")
    ok, errores = validar_registro_climatico(hoy, "1", "999", "60", "30", ZONAS)
    assert ok is False
    assert "temperatura" in errores

def test_registro_con_multiples_errores():
    ok, errores = validar_registro_climatico("mal-fecha", "99", "999", "-5", "-10", ZONAS)
    assert ok is False
    assert "fecha" in errores
    assert "zona" in errores
    assert "temperatura" in errores
    assert "humedad" in errores
    assert "viento" in errores

def test_registro_devuelve_todos_los_campos():
    hoy = datetime.now().strftime("%d-%m-%Y")
    ok, resultado = validar_registro_climatico(hoy, "3", "20", "50", "100", ZONAS)
    assert ok is True
    assert set(resultado.keys()) == {"fecha", "zona", "temperatura", "humedad", "viento"}