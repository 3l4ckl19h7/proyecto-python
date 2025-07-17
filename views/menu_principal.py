# from views.vista_registro import mostrar_formulario_registro
# from views.vista_consulta import mostrar_consulta
# from views.vista_registro_empleados import modulo_registro_empleados

# def mostrar_menu():
#     while True:
#         print("\n=== Menú Principal ===")
#         print("1. Registrar asistencia")
#         print("2. Consultar asistencia")
#         print("3. Registrar empleados")
#         print("4. Salir")

#         opcion = input("Selecciona una opción: ")

#         if opcion == "1":
#             mostrar_formulario_registro()
#         elif opcion == "2":
#             mostrar_consulta()
#         elif opcion == "3":
#             modulo_registro_empleados()
#         elif opcion == "4":
#             print("Gracias por usar el sistema. 🖐️")
#             break
#         else:
#             print("❌ Opción inválida.")

from tkinter import *
from views.vista_registro import mostrar_formulario_registro
from views.vista_consulta import mostrar_consulta
from views.vista_registro_empleados import modulo_registro_empleados

def mostrar_menu():
    ventana = Tk()
    ventana.title("Menú Principal")
    ventana.geometry("400x400")
    ventana.resizable(False, False)

    # Centrar ventana en la pantalla
    ancho = 400
    alto = 400
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # Título
    Label(ventana, text="Menú Principal", font=("Helvetica", 20, "bold")).pack(pady=30)

    # Botones
    Button(ventana, text="Registrar asistencia", width=25, height=2,
           bg="#4CAF50", fg="black", font=("Helvetica", 12, "bold"),
           command=mostrar_formulario_registro).pack(pady=10)

    Button(ventana, text="Consultar asistencia", width=25, height=2,
           bg="#2196F3", fg="black", font=("Helvetica", 12, "bold"),
           command=mostrar_consulta).pack(pady=10)

    Button(ventana, text="Registrar empleados", width=25, height=2,
           bg="#9C27B0", fg="black", font=("Helvetica", 12, "bold"),
           command=modulo_registro_empleados).pack(pady=10)

    Button(ventana, text="Salir", width=25, height=2,
           bg="#f44336", fg="black", font=("Helvetica", 12, "bold"),
           command=ventana.destroy).pack(pady=30)

    ventana.mainloop()

mostrar_menu()
