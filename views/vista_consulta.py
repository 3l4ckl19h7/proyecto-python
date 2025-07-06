from modules.consulta_asistencia import (
    obtener_asistencia_por_usuario,
    obtener_asistencia_por_fecha,
    obtener_asistencia_por_dni_y_fecha
 )
from utils.validaciones import (
    validar_dni,
    validar_fecha
)
from typing import List

def mostrar_tabla(asistencias: List[List[str]]) -> None:
    """Imprime los registros con encabezado y formato limpio en consola."""

    print("\n📋 HISTÓRICO DE ASISTENCIA\n")
    print(f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10} {'Fecha y hora':<20} {'Tardanza':<10} {'Estado':<10}")
    print("-" * 88)

    for fila in asistencias:
        print(f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10} {fila[4]:<20} {fila[5]:<10} {fila[6]:<10}")

def mostrar_consulta():

    while True:
        print("\n--- Módulo de Consulta de Asistencia ---")
        print("1. Buscar por DNI")
        print("2. Buscar por Fecha")
        print("3. Buscar por DNI y Fecha")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            dni = input("Ingrese DNI: ")
            if not validar_dni(dni): # True o False
                print("❌ DNI inválido.")
                continue
            registros = obtener_asistencia_por_usuario(dni)

        elif opcion == "2":
            fecha = input("Ingrese fecha (DD-MM-YYYY): ")
            if not validar_fecha(fecha):
                print("❌ Fecha inválida.")
                continue
            registros = obtener_asistencia_por_fecha(fecha)

        elif opcion == "3":
            dni = input("Ingrese DNI: ")
            fecha = input("Ingrese fecha (YYYY-MM-DD): ")
            if not validar_dni(dni) or not validar_fecha(fecha):
                print("❌ DNI o fecha inválida.")
                continue
            registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)

        elif opcion == "4":
            break

        else:
            print("\n⚠️ Opción inválida. Intenta nuevamente.")
            continue

        if registros:
            mostrar_tabla(registros)
        else:
            print("\n🔎 No se encontraron asistencias.")
            print("Verifique si ha digitado el DNI correctamente.")

    print("Estoy fuera del bucle de consulta")

    return


