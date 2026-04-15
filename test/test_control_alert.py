from controller.control_alert import obtener_alerta_temperatura, obtener_alerta_viento

# CODIGOS DE COLOR

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
NARANJA_REAL = "\033[38;5;208m"
RESET = "\033[0m"  # Vuelve al color original

def test_obtener_alerta_temperatura():
    assert obtener_alerta_temperatura(42) == f"{ROJO}ALERTA ROJA: {RESET} Riesgo extremo por calor - Riesgo para la salud muy alto. {RESET}"
    assert obtener_alerta_temperatura(-10) == f"{ROJO}ALERTA ROJA: {RESET} Frío extremo. Riesgo de heladas y nevadas severas. {RESET}"
    assert obtener_alerta_temperatura(39) == f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Riesgo importante por calor - Se recomienda no salir en horas centrales del día. {RESET}"
    assert obtener_alerta_temperatura(-6) == f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Temperaturas gélidas. Riesgo de heladas y nevadas. Peligro en tuberías y la salud. {RESET}"
    assert obtener_alerta_temperatura(36) == f"{AMARILLO}ALERTA AMARILLA: {RESET} Riesgo por calor - Se recomienda no realizar actividades al aire libre. {RESET}"
    assert obtener_alerta_temperatura(-4) == f"{AMARILLO}ALERTA AMARILLA: {RESET} Precaución por heladas. {RESET}"
    assert obtener_alerta_temperatura(25) == f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"

def test_obtener_alerta_viento():
    assert obtener_alerta_viento(110) == f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales. {RESET}"
    assert obtener_alerta_viento(90) == f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques. {RESET}"
    assert obtener_alerta_viento(70) == f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores. {RESET}"
    assert obtener_alerta_viento(50) == f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"

def test_invalido_alerta_viento():
    assert obtener_alerta_viento(110) != f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques. {RESET}"
    assert obtener_alerta_viento(90) != f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores. {RESET}"
    assert obtener_alerta_viento(70) != f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"
    assert obtener_alerta_viento(50) != f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales. {RESET}"

def test_invalido_alerta_temperatura():
    assert obtener_alerta_temperatura(42) != f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Temperaturas gélidas. Riesgo de heladas y nevadas. Peligro en tuberías y la salud. {RESET}"
    assert obtener_alerta_temperatura(-10) != f"{AMARILLO}ALERTA AMARILLA: {RESET} Precaución por heladas. {RESET}"
    assert obtener_alerta_temperatura(39) != f"{AMARILLO}ALERTA AMARILLA: {RESET} Riesgo por calor - Se recomienda no realizar actividades al aire libre. {RESET}"
    assert obtener_alerta_temperatura(-6) != f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"
    assert obtener_alerta_temperatura(36) != f"{ROJO}ALERTA ROJA: {RESET} Riesgo extremo por calor - Riesgo para la salud muy alto. {RESET}"
    assert obtener_alerta_temperatura(-4) != f"{ROJO}ALERTA ROJA: {RESET} Frío extremo. Riesgo de heladas y nevadas severas. {RESET}"
    assert obtener_alerta_temperatura(25) != f"{ROJO}ALERTA ROJA: {RESET} Riesgo extremo por calor - Riesgo para la salud muy alto. {RESET}"