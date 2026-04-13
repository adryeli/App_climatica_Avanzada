
# Importo os para trabajar con rutas y comprobar si existen archivos o carpetas
# Importo json para poder leer y escribir datos en formato JSON


import os
import json


def comprobar_archivo_json():
    """
    Esta función comprueba si existe el archivo data/register.json.
    Si no existe, crea la carpeta data/ y el archivo register.json
    con una lista vacía dentro.
    """

    # Defino la carpeta y el archivo
    carpeta = "data"
    ruta = os.path.join(carpeta, "register.json")

    # Si la carpeta no existe, la creo
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Si el archivo no existe, lo creo con una lista vacía
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)
             # "archivo" → es el archivo donde voy a escribir
            # indent=4 → hace que el JSON se guarde con formato bonito
             # ensure_ascii=False → permite guardar caracteres como tildes y ñ correctamente

    # Devuelvo la ruta para poder usarla en otras funciones
    return ruta


def leer_json():
    """
    Esta función lee el contenido del archivo JSON.
    Primero me aseguro de que el archivo existe.
    Después intento leerlo y devolver los datos.
    Si hay un error, devuelvo una lista vacía.
    """

    # Obtengo la ruta asegurándome de que el archivo existe
    ruta = comprobar_archivo_json()

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            if isinstance(datos, list):
                return datos

            return []

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def escribir_json(datos):
    """
    Esta función escribe los datos en el archivo JSON.
    """

    # Obtengo la ruta asegurándome de que el archivo existe
    ruta = comprobar_archivo_json()
    # Abro el archivo en modo escritura ("w"), esto significa que se va a sobrescribir
    # todo lo que hubiera antes en el archivo
    with open(ruta, "w", encoding="utf-8") as archivo:

    # json.dump sirve para convertir los datos de Python (por ejemplo una lista de diccionarios)
    # a formato JSON y guardarlos en el archivo
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    # "datos" → es la información que quiero guardar (normalmente una lista de registros)
   

def registro_valido(registro):
    """
    Esta función comprueba que el registro tenga la estructura correcta.
    Verifico que sea un diccionario y que tenga todas las claves necesarias.
    """

    # Defino las claves obligatorias que debe tener el registro
    claves_obligatorias = ["fecha", "zona", "temperatura", "humedad", "viento"]

    # Compruebo que el registro sea un diccionario
    if not isinstance(registro, dict):
        return False

    # Recorro las claves obligatorias y verifico que estén en el registro
    for clave in claves_obligatorias:
        if clave not in registro:
            return False

    # Si pasa todas las comprobaciones, el registro es válido
    return True
