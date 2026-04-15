ZONAS = {
    "1": "Centro",
    "2": "Norte",
    "3": "Sur",
    "4": "Este",
    "5": "Oeste"
}


def validar_opcion_menu(opcion):
    return opcion in {"1", "2", "3"}


def validar_opcion_zona(opcion):
    """
    Valida si la opción de zona es correcta.
    """
    return opcion in ZONAS
