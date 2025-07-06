from views.vista_registro import mostrar_formulario_registro
from views.vista_consulta import mostrar_consulta

def mostrar_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar asistencia")
        print("2. Consultar asistencia")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_formulario_registro()
        elif opcion == "2":
            mostrar_consulta()
        elif opcion == "3":
            print("Gracias por usar el sistema. 🖐️")
            break
        else:
            print("❌ Opción inválida.")
