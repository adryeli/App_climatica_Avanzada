# Importamos json para poder trabajar con archivos JSON
import json

# Importamos os para comprobar si un archivo existe
import os


class JsonManager:
    """
    Esta clase se encarga de gestionar archivos JSON.

    Es una pieza clave del MODELO (MVC), porque se encarga de la persistencia de datos.

    Responsabilidades:
    - Leer datos desde un archivo JSON
    - Guardar datos en un archivo JSON
    """

    def __init__(self, ruta):
        """
        Constructor de la clase.

        Parámetro:
        - ruta: ubicación del archivo JSON (por ejemplo: data/usuarios.json)
        """

        # Guardamos la ruta del archivo como atributo del objeto
        self.ruta = ruta

    def leer(self):
        """
        Lee el contenido del archivo JSON y lo devuelve como una lista.

        Este método es seguro:
        - Si el archivo no existe → devuelve []
        - Si está vacío → devuelve []
        - Si hay error en el JSON → devuelve []

        Esto evita que la aplicación se rompa.
        """

        # ---------------------------
        # COMPROBAR SI EL ARCHIVO EXISTE
        # ---------------------------

        # Si el archivo no existe, devolvemos lista vacía
        if not os.path.exists(self.ruta):
            return []

        try:
            # ---------------------------
            # ABRIR Y LEER EL ARCHIVO
            # ---------------------------

            # Abrimos el archivo en modo lectura
            # encoding="utf-8" permite usar tildes y caracteres especiales
            with open(self.ruta, "r", encoding="utf-8") as archivo:

                # Leemos el contenido y quitamos espacios innecesarios
                contenido = archivo.read().strip()

                # Si el archivo está vacío, devolvemos lista vacía
                if not contenido:
                    return []

                # Convertimos el texto JSON a estructura Python (lista o diccionario)
                return json.loads(contenido)

        except (json.JSONDecodeError, FileNotFoundError):
            """
            Si ocurre algún error:
            - JSON mal formado
            - archivo no encontrado

            devolvemos lista vacía para evitar que la app falle
            """
            return []

    def guardar(self, datos):
        """
        Guarda datos en el archivo JSON.

        Parámetro:
        - datos: lista o diccionario que queremos guardar

        IMPORTANTE:
        Este método sobrescribe el archivo completo,
        por eso antes normalmente se hace:
        leer → modificar → guardar
        """

        # ---------------------------
        # ESCRIBIR EN EL ARCHIVO
        # ---------------------------

        # Abrimos el archivo en modo escritura ("w")
        # Esto sobrescribe el contenido anterior
        with open(self.ruta, "w", encoding="utf-8") as archivo:

            # Convertimos los datos a formato JSON y los guardamos
            json.dump(
                datos,
                archivo,
                indent=4,          # Hace el JSON legible (formato bonito)
                ensure_ascii=False # Permite caracteres como ñ, tildes, etc.
            )