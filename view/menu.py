from controller.control_menu import validar_opcion_menu, validar_opcion_zona, ZONAS
from model.register_weather import guardar_registro, buscar_por_zona
from controller.control_time import (
    validar_fecha,
    validar_zona,
    validar_temperatura,
    validar_humedad,
    validar_viento,
    validar_registro_climatico
)
from controller.control_alert import obtener_alerta_temperatura, obtener_alerta_viento


def mostrar_menu():
    print("\n===== APP CLIMÁTICA =====")
    print("1. Registrar datos climáticos")
    print("2. Consultar datos por zona")
    print("3. Salir")


def pedir_opcion():
    while True:
        opcion = input("Selecciona una opción: ").strip()

        if validar_opcion_menu(opcion):
            return opcion

        print("❌ Opción no válida. Inténtalo de nuevo.")


def pedir_fecha():
    while True:
        fecha = input("Introduce la fecha (dd-mm-yyyy): ").strip()
        ok, resultado = validar_fecha(fecha)

        if ok:
            return resultado

        print(f"❌ {resultado}")


def pedir_zona():
    while True:
        print("\nSelecciona una zona:")
        print("1. Centro")
        print("2. Norte")
        print("3. Sur")
        print("4. Este")
        print("5. Oeste")

        opcion = input("Introduce el número de la zona: ").strip()

        if not validar_opcion_zona(opcion):
            print("❌ Opción de zona no válida. Inténtalo de nuevo.")
            continue

        zona = ZONAS[opcion]
        ok, resultado = validar_zona(zona, ZONAS.values())

        if ok:
            return resultado

        print(f"❌ {resultado}")


def pedir_temperatura():
    while True:
        valor = input("Introduce la temperatura (ºC): ").strip()
        ok, resultado = validar_temperatura(valor)

        if ok:
            return resultado

        print(f"❌ {resultado}")


def pedir_humedad():
    while True:
        valor = input("Introduce la humedad (%): ").strip()
        ok, resultado = validar_humedad(valor)

        if ok:
            return resultado

        print(f"❌ {resultado}")


def pedir_viento():
    while True:
        valor = input("Introduce el viento (km/h): ").strip()
        ok, resultado = validar_viento(valor)

        if ok:
            return resultado

        print(f"❌ {resultado}")


def volver_al_inicio():
    input("\nPulsa Enter para volver al menú principal...")


def mostrar_alertas(temperatura, viento):
    print("\n⚠️ ALERTAS CLIMÁTICAS")
    print("-" * 40)
    print(f"🌡 {obtener_alerta_temperatura(temperatura)}")
    print(f"🌬 {obtener_alerta_viento(viento)}")


def registrar_datos():
    print("\n===== REGISTRO DE DATOS CLIMÁTICOS =====")

    fecha = pedir_fecha()
    zona = pedir_zona()
    temperatura = pedir_temperatura()
    humedad = pedir_humedad()
    viento = pedir_viento()

    ok, resultado = validar_registro_climatico(
        fecha,
        zona,
        temperatura,
        humedad,
        viento,
        ZONAS.values()
    )

    if not ok:
        print("\n❌ Error al validar el registro:")
        for campo, error in resultado.items():
            print(f"- {campo}: {error}")
        volver_al_inicio()
        return

    registro = resultado

    if guardar_registro(registro):
        print("\n✅ DATOS GUARDADOS CORRECTAMENTE")
        print("=" * 40)
        print(f"📅 Fecha:         {registro['fecha']}")
        print(f"📍 Zona:          {registro['zona']}")
        print(f"🌡 Temperatura:   {registro['temperatura']} ºC")
        print(f"💧 Humedad:       {registro['humedad']} %")
        print(f"🌬 Viento:        {registro['viento']} km/h")
        print("=" * 40)

        mostrar_alertas(registro["temperatura"], registro["viento"])
    else:
        print("\n❌ No se pudieron guardar los datos.")

    volver_al_inicio()


def consultar_datos():
    print("\n===== CONSULTA DE DATOS POR ZONA =====")

    zona = pedir_zona()
    resultados = buscar_por_zona(zona)

    print(f"\n🔎 Has elegido consultar la zona: {zona}")

    if not resultados:
        print("\n❌ No hay registros guardados para esa zona.")
        volver_al_inicio()
        return

    print("\n📋 REGISTROS ENCONTRADOS")
    print("=" * 40)

    for i, registro in enumerate(resultados, start=1):
        print(f"\nRegistro {i}")
        print("-" * 25)
        print(f"📅 Fecha:         {registro['fecha']}")
        print(f"📍 Zona:          {registro['zona']}")
        print(f"🌡 Temperatura:   {registro['temperatura']} ºC")
        print(f"💧 Humedad:       {registro['humedad']} %")
        print(f"🌬 Viento:        {registro['viento']} km/h")
        print(f"🌡 Alerta temp.:  {obtener_alerta_temperatura(registro['temperatura'])}")
        print(f"🌬 Alerta viento: {obtener_alerta_viento(registro['viento'])}")

    print("\n" + "=" * 40)
    print(f"Total de registros: {len(resultados)}")

    volver_al_inicio()


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_datos()
        elif opcion == "2":
            consultar_datos()
        elif opcion == "3":
            print("\nSaliendo de la aplicación...")
            break