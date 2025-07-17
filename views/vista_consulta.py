# from modules.consulta_asistencia import (
#     obtener_asistencia_por_usuario,
#     obtener_asistencia_por_fecha,
#     obtener_asistencia_por_dni_y_fecha
#  )
# from utils.validaciones import (
#     validar_dni,
#     validar_fecha
# )
# from typing import List

# def mostrar_tabla(asistencias: List[List[str]]) -> None:
#     """Imprime los registros con encabezado y formato limpio en consola."""

#     print("\n📋 HISTÓRICO DE ASISTENCIA\n")
#     print(f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10} {'Fecha y hora':<20} {'Tardanza':<10} {'Estado':<10}")
#     print("-" * 88)

#     for fila in asistencias:
#         print(f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10} {fila[4]:<20} {fila[5]:<10} {fila[6]:<10}")

# def mostrar_consulta():

#     while True:
#         print("\n--- Módulo de Consulta de Asistencia ---")
#         print("1. Buscar por DNI")
#         print("2. Buscar por Fecha")
#         print("3. Buscar por DNI y Fecha")
#         print("4. Volver al menú principal")
#         opcion = input("Selecciona una opción (1-4): ")

#         if opcion == "1":
#             dni = input("Ingrese DNI: ")
#             if not validar_dni(dni): # True o False
#                 print("❌ DNI inválido.")
#                 continue
#             registros = obtener_asistencia_por_usuario(dni)

#         elif opcion == "2":
#             fecha = input("Ingrese fecha (DD-MM-YYYY): ")
#             if not validar_fecha(fecha):
#                 print("❌ Fecha inválida.")
#                 continue
#             registros = obtener_asistencia_por_fecha(fecha)

#         elif opcion == "3":
#             dni = input("Ingrese DNI: ")
#             fecha = input("Ingrese fecha (YYYY-MM-DD): ")
#             if not validar_dni(dni) or not validar_fecha(fecha):
#                 print("❌ DNI o fecha inválida.")
#                 continue
#             registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)

#         elif opcion == "4":
#             break

#         else:
#             print("\n⚠️ Opción inválida. Intenta nuevamente.")
#             continue

#         if registros:
#             mostrar_tabla(registros)
#         else:
#             print("\n🔎 No se encontraron asistencias.")
#             print("Verifique si ha digitado el DNI correctamente.")

#     print("Estoy fuera del bucle de consulta")

#     return

#------------------------------------------
# from tkinter import *
# from tkinter import messagebox, scrolledtext
# from modules.consulta_asistencia import (
#     obtener_asistencia_por_usuario,
#     obtener_asistencia_por_fecha,
#     obtener_asistencia_por_dni_y_fecha
# )
# from utils.validaciones import validar_dni, validar_fecha

# def mostrar_consulta():
#     ventana = Toplevel()
#     ventana.title("Consulta de Asistencia")
#     ventana.geometry("650x500")
#     ventana.resizable(False, False)

#     # Centrar ventana
#     ancho = 650
#     alto = 500
#     x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
#     y = (ventana.winfo_screenheight() // 2) - (alto // 2)
#     ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#     Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

#     frame_inputs = Frame(ventana)
#     frame_inputs.pack(pady=10)

#     # Entradas
#     Label(frame_inputs, text="DNI:").grid(row=0, column=0, padx=5, pady=5)
#     entry_dni = Entry(frame_inputs)
#     entry_dni.grid(row=0, column=1, padx=5)

#     Label(frame_inputs, text="Fecha (DD-MM-YYYY):").grid(row=1, column=0, padx=5, pady=5)
#     entry_fecha = Entry(frame_inputs)
#     entry_fecha.grid(row=1, column=1, padx=5)

#     # Área de resultados
#     resultado = scrolledtext.ScrolledText(ventana, width=80, height=15, font=("Courier", 10))
#     resultado.pack(pady=10)

#     def mostrar_tabla(asistencias):
#         resultado.delete(1.0, END)
#         encabezado = f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10} {'Fecha y hora':<20} {'Tardanza':<10} {'Estado':<10}\n"
#         resultado.insert(END, encabezado)
#         resultado.insert(END, "-" * 88 + "\n")
#         for fila in asistencias:
#             linea = f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10} {fila[4]:<20} {fila[5]:<10} {fila[6]:<10}\n"
#             resultado.insert(END, linea)

#     # Funciones de búsqueda
#     def buscar_por_dni():
#         dni = entry_dni.get().strip()
#         if not validar_dni(dni):
#             messagebox.showerror("Error", "❌ DNI inválido.")
#             return
#         registros = obtener_asistencia_por_usuario(dni)
#         if registros:
#             mostrar_tabla(registros)
#         else:
#             resultado.delete(1.0, END)
#             resultado.insert(END, "🔎 No se encontraron asistencias.\n")

#     def buscar_por_fecha():
#         fecha = entry_fecha.get().strip()
#         if not validar_fecha(fecha):
#             messagebox.showerror("Error", "❌ Fecha inválida. Usa DD-MM-YYYY.")
#             return
#         registros = obtener_asistencia_por_fecha(fecha)
#         if registros:
#             mostrar_tabla(registros)
#         else:
#             resultado.delete(1.0, END)
#             resultado.insert(END, "🔎 No se encontraron asistencias.\n")

#     def buscar_por_dni_y_fecha():
#         dni = entry_dni.get().strip()
#         fecha = entry_fecha.get().strip()
#         if not validar_dni(dni) or not validar_fecha(fecha):
#             messagebox.showerror("Error", "❌ DNI o Fecha inválida.")
#             return
#         registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)
#         if registros:
#             mostrar_tabla(registros)
#         else:
#             resultado.delete(1.0, END)
#             resultado.insert(END, "🔎 No se encontraron asistencias.\n")

#     # Botones de búsqueda
#     frame_botones = Frame(ventana)
#     frame_botones.pack(pady=10)

#     Button(frame_botones, text="Buscar por DNI", width=20, command=buscar_por_dni).grid(row=0, column=0, padx=5)
#     Button(frame_botones, text="Buscar por Fecha", width=20, command=buscar_por_fecha).grid(row=0, column=1, padx=5)
#     Button(frame_botones, text="Buscar por DNI y Fecha", width=25, command=buscar_por_dni_y_fecha).grid(row=0, column=2, padx=5)

#     Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

from tkinter import *
from tkinter import messagebox, scrolledtext
from modules.consulta_asistencia import (
    obtener_asistencia_por_usuario,
    obtener_asistencia_por_fecha,
    obtener_asistencia_por_dni_y_fecha
)
from utils.validaciones import validar_dni, validar_fecha
from datetime import datetime

def convertir_fecha_a_ddmmyyyy(fecha_str):
    """Convierte una fecha en formato YYYY-MM-DD a DD-MM-YYYY si es necesario."""
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha_obj.strftime("%d-%m-%Y")
    except:
        return fecha_str.strip()

def mostrar_consulta():
    ventana = Toplevel()
    ventana.title("Consulta de Asistencia")
    ventana.geometry("700x580")
    ventana.resizable(False, False)

    # Centrar ventana
    ancho = 700
    alto = 580
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

    frame_botones = Frame(ventana)
    frame_botones.pack(pady=10)

    tipo_busqueda = StringVar()
    ultimos_registros = []

    # Entradas ocultas por defecto
    frame_inputs = Frame(ventana)
    frame_inputs.pack()

    label_dni = Label(frame_inputs, text="DNI:")
    entry_dni = Entry(frame_inputs)

    label_fecha = Label(frame_inputs, text="Fecha (DD-MM-YYYY):")
    entry_fecha = Entry(frame_inputs)

    def mostrar_campos(tipo):
        tipo_busqueda.set(tipo)
        entry_dni.delete(0, END)
        entry_fecha.delete(0, END)

        label_dni.pack_forget()
        entry_dni.pack_forget()
        label_fecha.pack_forget()
        entry_fecha.pack_forget()
        boton_buscar.pack_forget()

        if tipo == "dni":
            label_dni.pack()
            entry_dni.pack()
        elif tipo == "fecha":
            label_fecha.pack()
            entry_fecha.pack()
        elif tipo == "ambos":
            label_dni.pack()
            entry_dni.pack()
            label_fecha.pack()
            entry_fecha.pack()

        boton_buscar.pack(pady=10)

    Button(frame_botones, text="Buscar por DNI", width=20,
           command=lambda: mostrar_campos("dni")).grid(row=0, column=0, padx=5)
    Button(frame_botones, text="Buscar por Fecha", width=20,
           command=lambda: mostrar_campos("fecha")).grid(row=0, column=1, padx=5)
    Button(frame_botones, text="Buscar por DNI y Fecha", width=25,
           command=lambda: mostrar_campos("ambos")).grid(row=0, column=2, padx=5)

    resultado = scrolledtext.ScrolledText(ventana, width=85, height=15, font=("Courier", 10))
    resultado.pack(pady=10)

    def mostrar_tabla(asistencias):
        resultado.delete(1.0, END)
        encabezado = f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10} {'Fecha y hora':<20} {'Tardanza':<10} {'Estado':<10}\n"
        resultado.insert(END, encabezado)
        resultado.insert(END, "-" * 88 + "\n")
        for fila in asistencias:
            linea = f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10} {fila[4]:<20} {fila[5]:<10} {fila[6]:<10}\n"
            resultado.insert(END, linea)

    def ejecutar_busqueda():
        tipo = tipo_busqueda.get()
        dni = entry_dni.get().strip()
        fecha = convertir_fecha_a_ddmmyyyy(entry_fecha.get().strip())

        registros = []

        if tipo == "dni":
            if not validar_dni(dni):
                messagebox.showerror("Error", "❌ DNI inválido.")
                return
            registros = obtener_asistencia_por_usuario(dni)

        elif tipo == "fecha":
            if not validar_fecha(fecha):
                messagebox.showerror("Error", "❌ Fecha inválida.")
                return
            registros = obtener_asistencia_por_fecha(fecha)

        elif tipo == "ambos":
            if not validar_dni(dni) or not validar_fecha(fecha):
                messagebox.showerror("Error", "❌ DNI o Fecha inválida.")
                return
            registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)

        else:
            messagebox.showwarning("Advertencia", "Selecciona un tipo de búsqueda primero.")
            return

        ultimos_registros.clear()
        ultimos_registros.extend(registros)

        if registros:
            mostrar_tabla(registros)
        else:
            resultado.delete(1.0, END)
            resultado.insert(END, "🔎 No se encontraron asistencias.\n")

    def ver_en_popup():
        if not ultimos_registros:
            messagebox.showinfo("Sin datos", "No hay registros para mostrar.")
            return

        texto = "📋 HISTÓRICO DE ASISTENCIA\n\n"
        texto += f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10}\n"
        texto += "-" * 50 + "\n"
        for fila in ultimos_registros:
            texto += f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10}\n"

        messagebox.showinfo("Registros encontrados", texto)

    boton_buscar = Button(ventana, text="Buscar", width=20, bg="#4CAF50", fg="white",
                          font=("Helvetica", 12, "bold"), command=ejecutar_busqueda)

    Button(ventana, text="Ver resumen en ventana emergente", bg="#2196F3", fg="white",
           font=("Helvetica", 10), command=ver_en_popup).pack(pady=5)

    Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)
