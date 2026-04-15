from datetime import datetime

def validar_fecha(fecha):
    """
    Valida que la fecha tenga formato YYYY-MM-DD
    y que no sea una fecha futura.
    """

    try:
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")

        # No permitir fechas futuras
        if fecha_obj > datetime.now():
            return False

        return True

    except ValueError:
        return False


def validar_zona(zona):
    """
    Valida que la zona no esté vacía y tenga longitud razonable.
    """

    return (
        zona is not None
        and zona.strip() != ""
        and len(zona.strip()) <= 50  # evitar textos absurdos
    )


def validar_temperatura(valor):
    """
    Valida temperatura:
    - Debe ser número
    - Rango realista: -50 a 60 ºC
    """

    try:
        temp = float(valor)
        return -50 <= temp <= 60

    except ValueError:
        return False


def validar_humedad(valor):
    """
    Valida humedad:
    - Número
    - Entre 0 y 100 %
    """

    try:
        humedad = float(valor)
        return 0 <= humedad <= 100

    except ValueError:
        return False


def validar_viento(valor):
    """
    Valida viento:
    - Número
    - No negativo
    - Máximo realista: 500 km/h 
    """

    try:
        viento = float(valor)
        return 0 <= viento <= 500

    except ValueError:
        return False


def validar_lluvia(valor):
    """
    Valida lluvia:
    - Número
    - No negativa
    - Máximo realista: 1000 mm (evento extremo)
    """

    try:
        lluvia = float(valor)
        return 0 <= lluvia <= 1000

    except ValueError:
        return False