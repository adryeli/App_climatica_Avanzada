import numpy as np
from model.manager import leer_json, escribir_json, registro_valido


def extraer_valores(registros, clave):
    # Devuelve una lista con los valores de la variable indicada
    # Ejemplo de clave: "temperatura", "humedad" o "viento"
    return [r[clave] for r in registros if clave in r]


def procesar_estadisticas(lista_valores):
    # Convertimos la lista de Python a un array de NumPy
    # Esto nos permite usar funciones matemáticas avanzadas
    arr = np.array(lista_valores)

    # Si no hay datos, devolvemos valores por defecto
    # Evita errores al usar np.mean, np.max, etc.
    if len(arr) == 0:
        return {
            "media": 0,
            "desviacion": 0,
            "maxima": 0,
            "minima": 0,
            "total": 0
        }

    # Calculamos estadísticas básicas (estadística descriptiva)
    return {
        "media": round(np.mean(arr), 2),          # Promedio
        "desviacion": round(np.std(arr), 2),      # Desviación estándar
        "maxima": float(np.max(arr)),             # Valor máximo
        "minima": float(np.min(arr)),             # Valor mínimo
        "total": len(arr)                         # Número de datos
    }


def detectar_anormalias(lista_valores):
    # Convertimos a array de NumPy
    arr = np.array(lista_valores)

    # Si no hay datos, no hay anomalías
    if len(arr) == 0:
        return []

    # Calculamos media y desviación estándar
    media = np.mean(arr)
    std = np.std(arr)

    # Si todos los valores son iguales (std = 0), no hay anomalías
    if std == 0:
        return []

    # Regla de las 3 desviaciones estándar:
    # Un valor es anómalo si está muy lejos de la media
    # np.abs() mide la distancia sin importar el signo (+ o -)
    anormalias = arr[np.abs(arr - media) > (3 * std)]

    # Convertimos el resultado a lista normal de Python
    return anormalias.tolist()


def simular_lluvias():
    # Distribución de Poisson:
    # Simula cuántas veces ocurre un evento en un intervalo (ej: lluvias por día)
    # lam = media de ocurrencias (1.2 lluvias por periodo)
    # size = cantidad de valores generados
    return np.random.poisson(lam=1.2, size=10).tolist()


def simular_evento_probabilidad():
    # Distribución binomial:
    # Simula número de éxitos en varios intentos
    # n = número de intentos (ej: 10 días)
    # p = probabilidad de éxito (ej: 70% de que haga sol)
    return np.random.binomial(n=10, p=0.7)


def informe_general(registros):
    # Sacamos los valores de cada variable climática
    temperaturas = extraer_valores(registros, "temperatura")
    humedades = extraer_valores(registros, "humedad")
    vientos = extraer_valores(registros, "viento")

    # Construimos un informe para cada variable
    return {
        "temperatura": {
            "estadisticas": procesar_estadisticas(temperaturas),
            "anormalias": detectar_anormalias(temperaturas)
        },
        "humedad": {
            "estadisticas": procesar_estadisticas(humedades),
            "anormalias": detectar_anormalias(humedades)
        },
        "viento": {
            "estadisticas": procesar_estadisticas(vientos),
            "anormalias": detectar_anormalias(vientos)
        }
    }


  
