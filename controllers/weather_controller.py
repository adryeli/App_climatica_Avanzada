# Importamos el gestor de JSON para leer y guardar registros
from models.json_manager import JsonManager

# Importamos la clase RegistroClima (POO)
# Representa cada registro meteorológico como un objeto
from models.registro_clima import RegistroClima

# Importamos el controlador de alertas
# Se encargará de comprobar si hay situaciones de riesgo
from controllers.alert_controller import AlertController

# Importamos las funciones de validación
# Cada una valida un campo del formulario
from utils.validators import (
    validar_fecha,
    validar_zona,
    validar_temperatura,
    validar_humedad,
    validar_viento,
    validar_lluvia
)

# Importamos las funciones de estadísticas
# calcular_estadisticas devuelve los datos numéricos
# generar_graficas crea imágenes para mostrarlas en la vista
from utils.stats import calcular_estadisticas, generar_graficas

# Importamos el sistema de logs
from utils.logger_config import configurar_logger

# Creamos el logger para registrar eventos
logger = configurar_logger()


class WeatherController:
    """
    Este controlador gestiona toda la lógica de los datos meteorológicos:
    - Guardar registros
    - Validar datos
    - Generar alertas
    - Consultar por zona
    - Calcular estadísticas
    """

    def __init__(self, ruta_registros="data/registros.json"):
        """
        Constructor de la clase.

        Inicializa:
        - el gestor del archivo JSON donde se guardan los registros
        - el controlador de alertas
        """
        self.json_manager = JsonManager(ruta_registros)
        self.alert_controller = AlertController()

    def guardar_registro(self, datos):
        """
        Guarda un nuevo registro meteorológico.

        Pasos:
        1. Obtener los datos del formulario
        2. Validar los datos
        3. Crear un objeto RegistroClima (POO)
        4. Comprobar alertas
        5. Guardar en JSON
        """

        # ---------------------------
        # 1. OBTENER DATOS DEL FORMULARIO
        # ---------------------------

        fecha = datos.get("fecha")
        zona = datos.get("zona")
        temperatura = datos.get("temperatura")
        humedad = datos.get("humedad")
        viento = datos.get("viento")
        lluvia = datos.get("lluvia")

        # ---------------------------
        # 2. VALIDACIONES
        # ---------------------------

        # Cada validación comprueba un campo concreto
        # Si alguna falla, se devuelve error y no se guarda nada

        if not validar_fecha(fecha):
            logger.warning("Validación fallida: fecha inválida")
            return False, "La fecha no es válida.", []

        if not validar_zona(zona):
            logger.warning(f"Validación fallida: zona inválida -> {zona}")
            return False, "La zona no es válida.", []

        if not validar_temperatura(temperatura):
            logger.warning(f"Validación fallida: temperatura inválida -> {temperatura}")
            return False, "La temperatura no es válida.", []

        if not validar_humedad(humedad):
            logger.warning(f"Validación fallida: humedad inválida -> {humedad}")
            return False, "La humedad debe estar entre 0 y 100.", []

        if not validar_viento(viento):
            logger.warning(f"Validación fallida: viento inválido -> {viento}")
            return False, "El viento no es válido.", []

        if not validar_lluvia(lluvia):
            logger.warning(f"Validación fallida: lluvia inválida -> {lluvia}")
            return False, "La lluvia no es válida.", []

        # ---------------------------
        # 3. CREAR OBJETO (POO)
        # ---------------------------

        # Creamos un objeto RegistroClima con los datos validados
        nuevo_registro = RegistroClima(
            fecha=fecha,
            zona=zona,
            temperatura=float(temperatura),
            humedad=float(humedad),
            viento=float(viento),
            lluvia=float(lluvia)
        )

        # ---------------------------
        # 4. COMPROBAR ALERTAS
        # ---------------------------

        # Convertimos el objeto a diccionario para usarlo en el AlertController
        alertas = self.alert_controller.comprobar_alertas(
            nuevo_registro.to_dict()
        )

        # Guardamos las alertas dentro del objeto
        nuevo_registro.alertas = alertas

        # Si hay alertas, se registran en logs
        if alertas:
            logger.warning(f"Alertas detectadas en {zona}: {alertas}")

        # ---------------------------
        # 5. GUARDAR EN JSON
        # ---------------------------

        # Leemos los registros actuales
        registros = self.json_manager.leer()

        # Añadimos el nuevo registro (convertido a diccionario)
        registros.append(nuevo_registro.to_dict())

        # Guardamos la lista actualizada
        self.json_manager.guardar(registros)

        # Registramos en logs que todo ha ido bien
        logger.info(f"Registro guardado correctamente -> {nuevo_registro.to_dict()}")

        return True, "Registro guardado correctamente.", alertas

    def consultar_por_zona(self, zona):
        """
        Devuelve una lista de registros filtrados por zona.
        """

        # Leemos todos los registros
        registros = self.json_manager.leer()

        # Filtramos solo los que coinciden con la zona (ignorando mayúsculas)
        resultados = [
            registro for registro in registros
            if registro.get("zona", "").lower() == zona.lower()
        ]

        # Guardamos en logs la consulta realizada
        logger.info(f"Consulta por zona: {zona} -> {len(resultados)} resultados")

        return resultados

    def obtener_estadisticas(self):
        """
        Obtiene estadísticas generales a partir de los registros almacenados.
        Además, genera las gráficas que luego se mostrarán en la vista.
        """

        # Leemos todos los registros
        registros = self.json_manager.leer()

        # Registramos en logs cuántos registros se van a procesar
        logger.info(f"Cálculo de estadísticas con {len(registros)} registros")

        # Generamos las gráficas en static/img
        generar_graficas(registros)

        # Devolvemos las estadísticas calculadas con pandas
        return calcular_estadisticas(registros)