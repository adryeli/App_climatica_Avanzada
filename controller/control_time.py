from datetime import datetime


def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str.strip(), "%d-%m-%Y")
        hoy = datetime.now()

        try:
            limite_pasado = hoy.replace(year=hoy.year - 10)
        except ValueError:
            
            limite_pasado = hoy.replace(year=hoy.year - 10, day=28)

        if fecha.date() > hoy.date():
            return False, "La fecha no puede ser futura."

        if fecha.date() < limite_pasado.date():
            return False, "La fecha no puede ser anterior a 10 años."

        return True, fecha.strftime("%d-%m-%Y")

    except (ValueError, AttributeError):
        return False, "Fecha inválida. Usa el formato DD-MM-YYYY."


def validar_zona(zona, zonas_validas):
    if not isinstance(zona, str) or not zona.strip():
        return False, "La zona no puede estar vacía."

    zona_limpia = zona.strip()

    if zona_limpia not in zonas_validas:
        return False, f"Zona inválida. Zonas permitidas: {', '.join(zonas_validas)}"

    return True, zona_limpia


def validar_temperatura(valor):
    try:
        temperatura = float(valor)
    except (ValueError, TypeError):
        return False, "La temperatura debe ser un número."

    if temperatura < -20 or temperatura > 50:
        return False, "La temperatura debe estar entre -20 y 50 ºC."

    return True, temperatura


def validar_humedad(valor):
    try:
        humedad = float(valor)
    except (ValueError, TypeError):
        return False, "La humedad debe ser un número."

    if humedad < 0 or humedad > 100:
        return False, "La humedad debe estar entre 0 y 100 %."

    return True, humedad


def validar_viento(valor):
    try:
        viento = float(valor)
    except (ValueError, TypeError):
        return False, "La velocidad del viento debe ser un número."

    if viento < 0:
        return False, "La velocidad del viento no puede ser negativa."

    if viento > 500:
        return False, "La velocidad del viento no puede superar 500 km/h."

    return True, viento


def validar_registro_climatico(fecha, zona, temperatura, humedad, viento, zonas_validas):
    errores = {}

    ok_fecha, resultado_fecha = validar_fecha(fecha)
    if not ok_fecha:
        errores["fecha"] = resultado_fecha

    ok_zona, resultado_zona = validar_zona(zona, zonas_validas)
    if not ok_zona:
        errores["zona"] = resultado_zona

    ok_temp, resultado_temp = validar_temperatura(temperatura)
    if not ok_temp:
        errores["temperatura"] = resultado_temp

    ok_humedad, resultado_humedad = validar_humedad(humedad)
    if not ok_humedad:
        errores["humedad"] = resultado_humedad

    ok_viento, resultado_viento = validar_viento(viento)
    if not ok_viento:
        errores["viento"] = resultado_viento

    if errores:
        return False, errores

    registro_validado = {
        "fecha": resultado_fecha,
        "zona": resultado_zona,
        "temperatura": resultado_temp,
        "humedad": resultado_humedad,
        "viento": resultado_viento,
    }

    return True, registro_validado
