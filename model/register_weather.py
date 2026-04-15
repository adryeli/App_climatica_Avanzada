from model.manager import leer_json, escribir_json, registro_valido

# Importo las funciones que necesito desde Manager.py
# leer_json() me devuelve la lista de registros guardados
# escribir_json(datos) guarda la lista completa en el archivo JSON
# registro_valido(registro) comprueba que el registro tenga la estructura correcta


def guardar_registro(registro):
    """
    Esta función guarda un nuevo registro en el archivo JSON.
    Primero compruebo si el registro es válido.
    Si no lo es, devuelvo False.
    Si es válido, leo los registros actuales, añado el nuevo
    y vuelvo a guardar la lista completa.
    """

    # Compruebo que el registro tenga la estructura correcta
    if not registro_valido(registro):
        return False

    # Leo todos los registros que ya están guardados en el JSON
    registros = leer_json()

    # Añado el nuevo registro a la lista
    registros.append(registro)

    # Guardo de nuevo la lista completa actualizada
    escribir_json(registros)

    # Si todo sale bien, devuelvo True
    return True


def obtener_registros():
    """
    Esta función devuelve todos los registros guardados.
    Simplemente lee el JSON y devuelve su contenido.
    """

    # Devuelvo todos los registros almacenados en el archivo JSON
    return leer_json()


def buscar_por_fecha(fecha):
    """
    Esta función busca los registros que coincidan con una fecha concreta.
    Recorro todos los registros y guardo en una lista
    solo los que tengan la misma fecha.
    """

    # Leo todos los registros guardados
    registros = leer_json()

    # Creo una lista vacía para guardar los resultados encontrados
    resultados = []

    # Recorro todos los registros uno por uno
    for registro in registros:

        # Si la fecha del registro coincide con la fecha buscada, lo añado a resultados
        if registro["fecha"] == fecha:
            resultados.append(registro)

    # Devuelvo la lista de registros encontrados
    return resultados


def buscar_por_zona(zona):
    """
    Esta función busca los registros que coincidan con una zona concreta.
    Comparo el valor guardado con la zona que recibo como parámetro.
    Uso lower() para que no importe si está en mayúsculas o minúsculas.
    """

    # Leo todos los registros guardados
    registros = leer_json()

    # Creo una lista vacía para guardar los resultados encontrados
    resultados = []

    # Recorro todos los registros uno por uno
    for registro in registros:

        # Comparo la zona del registro con la zona buscada sin distinguir mayúsculas y minúsculas
        if registro["zona"].lower() == zona.lower():
            resultados.append(registro)

    # Devuelvo la lista de registros encontrados
    return resultados


def eliminar_registros():
    """
    Esta función borra todos los registros del archivo JSON.
    Para hacerlo, escribo una lista vacía en el archivo.
    """

    # Sobrescribo el archivo JSON con una lista vacía
    escribir_json([])

    # Devuelvo True para indicar que la operación se ha realizado
    return True