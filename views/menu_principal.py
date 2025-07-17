from views.vista_registro import mostrar_formulario_registro
from views.vista_consulta import mostrar_consulta
from views.vista_registro_empleados import modulo_registro_empleados
from views.vista_consulta_empleados import modulo_consulta_empleados

def mostrar_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar asistencia")
        print("2. Consultar asistencia")
        print("3. Registrar empleados")
        print("4. Consultar empleados")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_formulario_registro()
        elif opcion == "2":
            mostrar_consulta()
        elif opcion == "3":
            modulo_registro_empleados()
        elif opcion == "4":
            modulo_consulta_empleados()
            print("Estos son nuestros empleados, gracias. 🖐️")
            break
        elif opcion == "5":
            print("Gracias por usar el sistema. 🖐️")
            break
        else:
            print("❌ Opción inválida.")
