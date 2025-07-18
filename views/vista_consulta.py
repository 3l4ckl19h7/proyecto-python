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

#--------------


# from tkinter import *
# from tkinter import messagebox, scrolledtext
# from modules.consulta_asistencia import (
#     obtener_asistencia_por_usuario,
#     obtener_asistencia_por_fecha,
#     obtener_asistencia_por_dni_y_fecha
# )
# from utils.validaciones import validar_dni, validar_fecha
# from datetime import datetime

# def convertir_fecha_a_ddmmyyyy(fecha_str):
#     """Convierte una fecha en formato YYYY-MM-DD a DD-MM-YYYY si es necesario."""
#     try:
#         fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
#         return fecha_obj.strftime("%d-%m-%Y")
#     except:
#         return fecha_str.strip()

# def mostrar_consulta():
#     ventana = Toplevel()
#     ventana.title("Consulta de Asistencia")
#     ventana.geometry("700x580")
#     ventana.resizable(False, False)

#     # Centrar ventana
#     ancho = 800
#     alto = 580
#     x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
#     y = (ventana.winfo_screenheight() // 2) - (alto // 2)
#     ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#     Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

#     frame_botones = Frame(ventana)
#     frame_botones.pack(pady=10)

#     tipo_busqueda = StringVar()
#     ultimos_registros = []

#     # Entradas ocultas por defecto
#     frame_inputs = Frame(ventana)
#     frame_inputs.pack()

#     label_dni = Label(frame_inputs, text="DNI:")
#     entry_dni = Entry(frame_inputs)

#     label_fecha = Label(frame_inputs, text="Fecha (DD-MM-YYYY):")
#     entry_fecha = Entry(frame_inputs)

#     def mostrar_campos(tipo):
#         tipo_busqueda.set(tipo)
#         entry_dni.delete(0, END)
#         entry_fecha.delete(0, END)

#         label_dni.pack_forget()
#         entry_dni.pack_forget()
#         label_fecha.pack_forget()
#         entry_fecha.pack_forget()
#         boton_buscar.pack_forget()

#         if tipo == "dni":
#             label_dni.pack()
#             entry_dni.pack()
#         elif tipo == "fecha":
#             label_fecha.pack()
#             entry_fecha.pack()
#         elif tipo == "ambos":
#             label_dni.pack()
#             entry_dni.pack()
#             label_fecha.pack()
#             entry_fecha.pack()

#         boton_buscar.pack(pady=10)

#     Button(frame_botones, text="Buscar por DNI", width=20,
#            command=lambda: mostrar_campos("dni")).grid(row=0, column=0, padx=5)
#     Button(frame_botones, text="Buscar por Fecha", width=20,
#            command=lambda: mostrar_campos("fecha")).grid(row=0, column=1, padx=5)
#     Button(frame_botones, text="Buscar por DNI y Fecha", width=25,
#            command=lambda: mostrar_campos("ambos")).grid(row=0, column=2, padx=5)

#     resultado = scrolledtext.ScrolledText(ventana, width=85, height=15, font=("Courier", 10))
#     resultado.pack(pady=10)

#     def mostrar_tabla(asistencias):
#         resultado.delete(1.0, END)
#         encabezado = f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10} {'Fecha y hora':<20} {'Tardanza':<10} {'Estado':<10}\n"
#         resultado.insert(END, encabezado)
#         resultado.insert(END, "-" * 88 + "\n")
#         for fila in asistencias:
#             linea = f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10} {fila[4]:<20} {fila[5]:<10} {fila[6]:<10}\n"
#             resultado.insert(END, linea)

#     def ejecutar_busqueda():
#         tipo = tipo_busqueda.get()
#         dni = entry_dni.get().strip()
#         fecha = convertir_fecha_a_ddmmyyyy(entry_fecha.get().strip())

#         registros = []

#         if tipo == "dni":
#             if not validar_dni(dni):
#                 messagebox.showerror("Error", "❌ DNI inválido.")
#                 return
#             registros = obtener_asistencia_por_usuario(dni)

#         elif tipo == "fecha":
#             if not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_fecha(fecha)

#         elif tipo == "ambos":
#             if not validar_dni(dni) or not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ DNI o Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)

#         else:
#             messagebox.showwarning("Advertencia", "Selecciona un tipo de búsqueda primero.")
#             return

#         ultimos_registros.clear()
#         ultimos_registros.extend(registros)

#         if registros:
#             mostrar_tabla(registros)
#         else:
#             resultado.delete(1.0, END)
#             resultado.insert(END, "🔎 No se encontraron asistencias.\n")

#     def ver_en_popup():
#         if not ultimos_registros:
#             messagebox.showinfo("Sin datos", "No hay registros para mostrar.")
#             return

#         texto = "📋 HISTÓRICO DE ASISTENCIA\n\n"
#         texto += f"{'DNI':<10} {'Apellidos':<12} {'Nombres':<12} {'Día':<10}\n"
#         texto += "-" * 50 + "\n"
#         for fila in ultimos_registros:
#             texto += f"{fila[0]:<10} {fila[1]:<12} {fila[2]:<12} {fila[3]:<10}\n"

#         messagebox.showinfo("Registros encontrados", texto)

#     boton_buscar = Button(ventana, text="Buscar", width=20, bg="#4CAF50", fg="white",
#                           font=("Helvetica", 12, "bold"), command=ejecutar_busqueda)

#     Button(ventana, text="Ver resumen en ventana emergente", bg="#2196F3", fg="white",
#            font=("Helvetica", 10), command=ver_en_popup).pack(pady=5)

#     Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)


# from tkinter import *
# from tkinter import ttk, messagebox
# from modules.consulta_asistencia import (
#     obtener_asistencia_por_usuario,
#     obtener_asistencia_por_fecha,
#     obtener_asistencia_por_dni_y_fecha
# )
# from utils.validaciones import validar_dni, validar_fecha
# from datetime import datetime

# def convertir_fecha_a_ddmmyyyy(fecha_str):
#     """Convierte una fecha en formato YYYY-MM-DD a DD-MM-YYYY si es necesario."""
#     try:
#         fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
#         return fecha_obj.strftime("%d-%m-%Y")
#     except:
#         return fecha_str.strip()

# def mostrar_consulta():
#     ventana = Toplevel()
#     ventana.title("Consulta de Asistencia")
#     ventana.geometry("800x580")
#     ventana.resizable(False, False)

#     # Centrar ventana
#     ancho = 800
#     alto = 580
#     x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
#     y = (ventana.winfo_screenheight() // 2) - (alto // 2)
#     ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#     Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

#     frame_botones = Frame(ventana)
#     frame_botones.pack(pady=10)

#     tipo_busqueda = StringVar()
#     ultimos_registros = []

#     # Entradas ocultas por defecto
#     frame_inputs = Frame(ventana)
#     frame_inputs.pack()

#     label_dni = Label(frame_inputs, text="DNI:")
#     entry_dni = Entry(frame_inputs)

#     label_fecha = Label(frame_inputs, text="Fecha (DD-MM-YYYY):")
#     entry_fecha = Entry(frame_inputs)

#     def mostrar_campos(tipo):
#         tipo_busqueda.set(tipo)
#         entry_dni.delete(0, END)
#         entry_fecha.delete(0, END)

#         label_dni.pack_forget()
#         entry_dni.pack_forget()
#         label_fecha.pack_forget()
#         entry_fecha.pack_forget()
#         boton_buscar.pack_forget()

#         if tipo == "dni":
#             label_dni.pack()
#             entry_dni.pack()
#         elif tipo == "fecha":
#             label_fecha.pack()
#             entry_fecha.pack()
#         elif tipo == "ambos":
#             label_dni.pack()
#             entry_dni.pack()
#             label_fecha.pack()
#             entry_fecha.pack()

#         boton_buscar.pack(pady=10)

#     Button(frame_botones, text="Buscar por DNI", width=20,
#            command=lambda: mostrar_campos("dni")).grid(row=0, column=0, padx=5)
#     Button(frame_botones, text="Buscar por Fecha", width=20,
#            command=lambda: mostrar_campos("fecha")).grid(row=0, column=1, padx=5)
#     Button(frame_botones, text="Buscar por DNI y Fecha", width=25,
#            command=lambda: mostrar_campos("ambos")).grid(row=0, column=2, padx=5)

#     # Tabla de resultados en la ventana principal
#     frame_tabla = Frame(ventana)
#     frame_tabla.pack(pady=10, fill=BOTH, expand=True)

#     columnas = ["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"]
#     tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)

#     for col in columnas:
#         tabla.heading(col, text=col)
#         tabla.column(col, width=100, anchor=W)

#     scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
#     tabla.configure(yscroll=scroll_y.set)
#     tabla.grid(row=0, column=0, sticky="nsew")
#     scroll_y.grid(row=0, column=1, sticky="ns")
#     frame_tabla.grid_rowconfigure(0, weight=1)
#     frame_tabla.grid_columnconfigure(0, weight=1)

#     def ejecutar_busqueda():
#         tipo = tipo_busqueda.get()
#         dni = entry_dni.get().strip()
#         fecha = convertir_fecha_a_ddmmyyyy(entry_fecha.get().strip())

#         registros = []

#         if tipo == "dni":
#             if not validar_dni(dni):
#                 messagebox.showerror("Error", "❌ DNI inválido.")
#                 return
#             registros = obtener_asistencia_por_usuario(dni)

#         elif tipo == "fecha":
#             if not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_fecha(fecha)

#         elif tipo == "ambos":
#             if not validar_dni(dni) or not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ DNI o Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)

#         else:
#             messagebox.showwarning("Advertencia", "Selecciona un tipo de búsqueda primero.")
#             return

#         ultimos_registros.clear()
#         ultimos_registros.extend(registros)

#         # Limpiar la tabla y mostrar resultados
#         for item in tabla.get_children():
#             tabla.delete(item)
#         if registros:
#             for fila in registros:
#                 fila_c = list(fila)[:7] + [""] * (7 - len(fila))
#                 tabla.insert("", "end", values=fila_c[:7])
#         else:
#             messagebox.showinfo("Resultado", "🔎 No se encontraron asistencias.")

#     def ver_en_popup():
#         """Muestra los últimos registros en una ventana emergente con tabla tipo Treeview."""
#         if not ultimos_registros:
#             messagebox.showinfo("Sin datos", "No hay registros para mostrar.")
#             return

#         pop = Toplevel(ventana)
#         pop.title("Histórico de Asistencias (Registros encontrados)")
#         pop.geometry("1100x500")
#         pop.grab_set()
#         pop.configure(bg="#F8F9F9")

#         # Centrar
#         ancho = 1100
#         alto = 500
#         x = (pop.winfo_screenwidth() // 2) - (ancho // 2)
#         y = (pop.winfo_screenheight() // 2) - (alto // 2)
#         pop.geometry(f"{ancho}x{alto}+{x}+{y}")

#         Label(pop, text="Histórico de Asistencias",
#               font=("Helvetica", 18, "bold"), bg="#F8F9F9", fg="#2C3E50").pack(pady=(15, 5))

#         Label(pop, text=f"Total de registros: {len(ultimos_registros)}",
#               font=("Helvetica", 12), bg="#F8F9F9", fg="#555555").pack(pady=(0, 10))

#         cont_tabla = Frame(pop, bg="#F8F9F9")
#         cont_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

#         tabla_popup = ttk.Treeview(cont_tabla, columns=columnas, show="headings", height=15)

#         for col in columnas:
#             tabla_popup.heading(col, text=col)
#             tabla_popup.column(col, width=150, anchor=W)

#         scroll_y = ttk.Scrollbar(cont_tabla, orient=VERTICAL, command=tabla_popup.yview)
#         scroll_x = ttk.Scrollbar(cont_tabla, orient=HORIZONTAL, command=tabla_popup.xview)
#         tabla_popup.configure(yscroll=scroll_y.set, xscroll=scroll_x.set)

#         tabla_popup.grid(row=0, column=0, sticky="nsew")
#         scroll_y.grid(row=0, column=1, sticky="ns")
#         scroll_x.grid(row=1, column=0, sticky="ew")
#         cont_tabla.grid_rowconfigure(0, weight=1)
#         cont_tabla.grid_columnconfigure(0, weight=1)

#         for fila in ultimos_registros:
#             fila_c = list(fila)[:7] + [""] * (7 - len(fila))
#             tabla_popup.insert("", "end", values=fila_c[:7])

#         Button(pop, text="Cerrar", command=pop.destroy,
#                bg="#C0392B", fg="white", font=("Helvetica", 12, "bold"), width=15).pack(pady=10)

#     boton_buscar = Button(ventana, text="Buscar", width=20, bg="#4CAF50", fg="white",
#                           font=("Helvetica", 12, "bold"), command=ejecutar_busqueda)
#     Button(ventana, text="Ver resumen en ventana emergente", bg="#2196F3", fg="white",
#            font=("Helvetica", 10), command=ver_en_popup).pack(pady=5)

#     boton_buscar.pack(pady=10)
#     Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)

#----------------
# from tkinter import *
# from tkinter import ttk, messagebox, filedialog
# from modules.consulta_asistencia import (
#     obtener_asistencia_por_usuario,
#     obtener_asistencia_por_fecha,
#     obtener_asistencia_por_dni_y_fecha
# )
# from utils.validaciones import validar_dni, validar_fecha
# from datetime import datetime

# def convertir_fecha_a_ddmmyyyy(fecha_str):
#     try:
#         fecha_obj = datetime.strptime(fecha_str.strip(), "%Y-%m-%d")
#         return fecha_obj.strftime("%d-%m-%Y")
#     except Exception:
#         return fecha_str.strip()

# def exportar_asistencias_a_pdf(registros, ruta_pdf):
#     if not registros:
#         raise ValueError("No hay registros para exportar.")

#     try:
#         from reportlab.lib.pagesizes import A4, landscape
#         from reportlab.pdfgen import canvas
#         from reportlab.lib import colors
#         from reportlab.platypus import Table, TableStyle
#     except ImportError:
#         raise ImportError("Instala reportlab: pip install reportlab")

#     columnas = ["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"]
#     filas = [list(fila)[:7] + [""] * (7 - len(fila)) for fila in registros]

#     data = [columnas] + filas
#     page_size = landscape(A4)
#     ancho_pag, alto_pag = page_size
#     margin_x, margin_y = 40, 40
#     col_widths = [60, 110, 110, 60, 160, 80, 80]
#     row_height = 18

#     c = canvas.Canvas(ruta_pdf, pagesize=page_size)
#     titulo = "Histórico de Asistencias"
#     generado = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#     total = f"Total: {len(filas)}"
#     espacio_top, espacio_bottom = 90, 40
#     usable_height = alto_pag - espacio_top - espacio_bottom
#     filas_por_pagina = max(1, int(usable_height // row_height))

#     def dibujar_pagina(subfilas, pagina_num, num_paginas):
#         c.setFont("Helvetica-Bold", 16)
#         c.drawString(margin_x, alto_pag - 40, titulo)
#         c.setFont("Helvetica", 10)
#         c.drawString(margin_x, alto_pag - 58, total)
#         c.drawString(margin_x, alto_pag - 72, f"Generado: {generado}")
#         c.drawRightString(ancho_pag - margin_x, alto_pag - 58, f"Página {pagina_num}/{num_paginas}")

#         page_data = [columnas] + subfilas
#         t = Table(page_data, colWidths=col_widths, rowHeights=row_height)
#         style = TableStyle([
#             ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D5D8DC")),
#             ("ALIGN", (0, 0), (-1, -1), "LEFT"),
#             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#             ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
#         ])
#         t.setStyle(style)
#         x = margin_x
#         y = espacio_bottom + (usable_height - (row_height * len(page_data)))
#         y = max(y, margin_y)
#         t.wrapOn(c, ancho_pag - margin_x * 2, usable_height)
#         t.drawOn(c, x, y)
#         c.showPage()

#     sublistas = [filas[i:i + filas_por_pagina] for i in range(0, len(filas), filas_por_pagina)]
#     for idx, subfilas in enumerate(sublistas, start=1):
#         dibujar_pagina(subfilas, idx, len(sublistas))
#     c.save()

# def mostrar_consulta():
#     ventana = Toplevel()
#         # Hacer que esta ventana sea modal para que la principal no cambie ni se use
#     ventana.transient(ventana.master)  # asocia a la ventana raíz (si existe); si da error, usa solo ventana.transient()
#     ventana.grab_set()                 # bloquea interacción con la ventana principal
#     ventana.focus_set()                # foco a esta ventana

#     ventana.title("Consulta de Asistencia")
#     ventana.geometry("800x580")
#     ventana.resizable(False, False)

#     # Centrar ventana
#     ancho, alto = 1000, 580
#     x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
#     y = (ventana.winfo_screenheight() // 2) - (alto // 2)
#     ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#     Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

#     # Estilos
#     style = ttk.Style(ventana)
#     style.theme_use("clam")
#     style.configure("Green.TButton", font=("Helvetica", 12, "bold"),
#                     foreground="white", background="#4CAF50")
#     style.map("Green.TButton", background=[("active", "#66BB6A")])
#     style.configure("Blue.TButton", font=("Helvetica", 12, "bold"),
#                     foreground="white", background="#2196F3")
#     style.map("Blue.TButton", background=[("active", "#42A5F5")])
#     style.configure("Red.TButton", font=("Helvetica", 12, "bold"),
#                     foreground="white", background="#C0392B")
#     style.map("Red.TButton", background=[("active", "#E74C3C")])

#     tipo_busqueda = StringVar()
#     ultimos_registros = []

#     # Botones búsqueda
#     frame_botones = Frame(ventana)
#     frame_botones.pack(pady=10)
#     frame_inputs = Frame(ventana)
#     frame_inputs.pack()

#     label_dni, entry_dni = Label(frame_inputs, text="DNI:"), Entry(frame_inputs)
#     label_fecha, entry_fecha = Label(frame_inputs, text="Fecha (DD-MM-YYYY):"), Entry(frame_inputs)

#     def mostrar_campos(tipo):
#         tipo_busqueda.set(tipo)
#         entry_dni.delete(0, END)
#         entry_fecha.delete(0, END)
#         for w in [label_dni, entry_dni, label_fecha, entry_fecha]:
#             w.pack_forget()
#         if tipo == "dni":
#             label_dni.pack()
#             entry_dni.pack()
#         elif tipo == "fecha":
#             label_fecha.pack()
#             entry_fecha.pack()
#         elif tipo == "ambos":
#             label_dni.pack()
#             entry_dni.pack()
#             label_fecha.pack()
#             entry_fecha.pack()

#     ttk.Button(frame_botones, text="Buscar por DNI",
#                style="Green.TButton", width=20,
#                command=lambda: mostrar_campos("dni")).grid(row=0, column=0, padx=5)
#     ttk.Button(frame_botones, text="Buscar por Fecha",
#                style="Blue.TButton", width=20,
#                command=lambda: mostrar_campos("fecha")).grid(row=0, column=1, padx=5)
#     ttk.Button(frame_botones, text="Buscar por DNI y Fecha",
#                style="Red.TButton", width=25,
#                command=lambda: mostrar_campos("ambos")).grid(row=0, column=2, padx=5)

#     # Tabla
#     frame_tabla = Frame(ventana)
#     frame_tabla.pack(pady=10, fill=BOTH, expand=True)
#     columnas = ["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"]
#     tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
#     for col in columnas:
#         if col == "Fecha y hora":
#          tabla.heading(col, text=col)
#          tabla.column(col, width=200, anchor=W)
#         else:   
#          tabla.heading(col, text=col)
#          tabla.column(col, width=110, anchor=W)
#     scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
#     tabla.configure(yscroll=scroll_y.set)
#     tabla.grid(row=0, column=0, sticky="nsew")
#     scroll_y.grid(row=0, column=1, sticky="ns")
#     frame_tabla.grid_rowconfigure(0, weight=1)
#     frame_tabla.grid_columnconfigure(0, weight=1)

#     # Funciones
#     def ejecutar_busqueda():
#         tipo = tipo_busqueda.get()
#         dni, fecha = entry_dni.get().strip(), convertir_fecha_a_ddmmyyyy(entry_fecha.get().strip())
#         registros = []
#         if tipo == "dni":
#             if not validar_dni(dni):
#                 messagebox.showerror("Error", "❌ DNI inválido.")
#                 return
#             registros = obtener_asistencia_por_usuario(dni)
#         elif tipo == "fecha":
#             if not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_fecha(fecha)
#         elif tipo == "ambos":
#             if not validar_dni(dni) or not validar_fecha(fecha):
#                 messagebox.showerror("Error", "❌ DNI o Fecha inválida.")
#                 return
#             registros = obtener_asistencia_por_dni_y_fecha(dni, fecha)
#         else:
#             messagebox.showwarning("Advertencia", "Selecciona un tipo de búsqueda primero.")
#             return

#         ultimos_registros.clear()
#         ultimos_registros.extend(registros)
#         for item in tabla.get_children():
#             tabla.delete(item)
#         if registros:
#             for fila in registros:
#                 fila_c = list(fila)[:7] + [""] * (7 - len(fila))
#                 tabla.insert("", "end", values=fila_c[:7])
#         else:
#             messagebox.showinfo("Resultado", "🔎 No se encontraron asistencias.")

#     def generar_pdf():
#         if not ultimos_registros:
#             messagebox.showinfo("Sin datos", "No hay registros para exportar.")
#             return
#         sugerido = f"reporte_asistencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
#         ruta_pdf = filedialog.asksaveasfilename(title="Guardar reporte en PDF",
#                                                 defaultextension=".pdf",
#                                                 initialfile=sugerido,
#                                                 filetypes=[("PDF", "*.pdf"), ("Todos", "*.*")])
#         if not ruta_pdf:
#             return
#         try:
#             exportar_asistencias_a_pdf(ultimos_registros, ruta_pdf)
#             messagebox.showinfo("Éxito", f"PDF generado:\n{ruta_pdf}")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     # Frame para los tres botones
#     frame_botones_final = Frame(ventana)
#     frame_botones_final.pack(pady=15)

#     ttk.Button(frame_botones_final, text="Buscar",
#                style="Green.TButton", command=ejecutar_busqueda,
#                width=18).grid(row=0, column=0, padx=10)

#     ttk.Button(frame_botones_final, text="Generar PDF",
#                style="Blue.TButton", command=generar_pdf,
#                width=18).grid(row=0, column=1, padx=10)

#     ttk.Button(frame_botones_final, text="Cerrar",
#                style="Red.TButton", command=ventana.destroy,
#                width=18).grid(row=0, column=2, padx=10)

from tkinter import *
from tkinter import ttk, messagebox, filedialog
from modules.consulta_asistencia import (
    obtener_asistencia_por_usuario,
    obtener_asistencia_por_fecha,
    obtener_asistencia_por_dni_y_fecha
)
from utils.validaciones import validar_dni, validar_fecha
from datetime import datetime


def convertir_fecha_a_ddmmyyyy(fecha_str: str) -> str:
    """Convierte 'YYYY-MM-DD' a 'DD-MM-YYYY'. Si falla, retorna la cadena original limpia."""
    try:
        fecha_obj = datetime.strptime(fecha_str.strip(), "%Y-%m-%d")
        return fecha_obj.strftime("%d-%m-%Y")
    except Exception:
        return fecha_str.strip()


def exportar_asistencias_a_pdf(registros, ruta_pdf: str):
    """Exporta registros de asistencia a un PDF en formato paisaje."""
    if not registros:
        raise ValueError("No hay registros para exportar.")

    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors
        from reportlab.platypus import Table, TableStyle
    except ImportError:  # pragma: no cover - dependencia externa
        raise ImportError("Instala reportlab: pip install reportlab")

    columnas = ["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"]
    filas = [list(fila)[:7] + [""] * (7 - len(fila)) for fila in registros]

    data = [columnas] + filas
    page_size = landscape(A4)
    ancho_pag, alto_pag = page_size
    margin_x, margin_y = 40, 40
    col_widths = [60, 110, 110, 60, 160, 80, 80]
    row_height = 18

    c = canvas.Canvas(ruta_pdf, pagesize=page_size)
    titulo = "Histórico de Asistencias"
    generado = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    total = f"Total: {len(filas)}"
    espacio_top, espacio_bottom = 90, 40
    usable_height = alto_pag - espacio_top - espacio_bottom
    filas_por_pagina = max(1, int(usable_height // row_height))

    def dibujar_pagina(subfilas, pagina_num, num_paginas):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin_x, alto_pag - 40, titulo)
        c.setFont("Helvetica", 10)
        c.drawString(margin_x, alto_pag - 58, total)
        c.drawString(margin_x, alto_pag - 72, f"Generado: {generado}")
        c.drawRightString(ancho_pag - margin_x, alto_pag - 58, f"Página {pagina_num}/{num_paginas}")

        page_data = [columnas] + subfilas
        t = Table(page_data, colWidths=col_widths, rowHeights=row_height)
        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D5D8DC")),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ])
        t.setStyle(style)
        x = margin_x
        y = espacio_bottom + (usable_height - (row_height * len(page_data)))
        y = max(y, margin_y)
        t.wrapOn(c, ancho_pag - margin_x * 2, usable_height)
        t.drawOn(c, x, y)
        c.showPage()

    sublistas = [filas[i : i + filas_por_pagina] for i in range(0, len(filas), filas_por_pagina)]
    for idx, subfilas in enumerate(sublistas, start=1):
        dibujar_pagina(subfilas, idx, len(sublistas))
    c.save()


def mostrar_consulta():
    ventana = Toplevel()

    # --- Hacer que esta ventana sea modal para que la principal no cambie ni se use ---
    ventana.transient(ventana.master)  # asocia a la ventana raíz (si existe)
    ventana.grab_set()  # bloquea interacción con la ventana principal
    ventana.focus_set()  # foco a esta ventana

    ventana.title("Consulta de Asistencia")
    ventana.geometry("800x580")
    ventana.resizable(False, False)

    # Centrar ventana
    ancho, alto = 1000, 600
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    Label(ventana, text="Consulta de Asistencia", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Estilos -----------------------------------------------------------------
    style = ttk.Style(ventana)
    style.theme_use("clam")
    style.configure("Green.TButton", font=("Helvetica", 12, "bold"), foreground="white", background="#4CAF50")
    style.map("Green.TButton", background=[("active", "#66BB6A")])
    style.configure("Blue.TButton", font=("Helvetica", 12, "bold"), foreground="white", background="#2196F3")
    style.map("Blue.TButton", background=[("active", "#42A5F5")])
    style.configure("Red.TButton", font=("Helvetica", 12, "bold"), foreground="white", background="#C0392B")
    style.map("Red.TButton", background=[("active", "#E74C3C")])

    # Variables ----------------------------------------------------------------
    tipo_busqueda = StringVar(value="")  # empieza sin selección; el trace detectará cambios
    ultimos_registros = []

    # Marcos -------------------------------------------------------------------
    frame_botones = Frame(ventana)
    frame_botones.pack(pady=10)
    frame_inputs = Frame(ventana)
    frame_inputs.pack()

    label_dni = Label(frame_inputs, text="DNI:")
    entry_dni = Entry(frame_inputs)
    label_fecha = Label(frame_inputs, text="Fecha (DD-MM-YYYY):")
    entry_fecha = Entry(frame_inputs)

    # Tabla --------------------------------------------------------------------
    frame_tabla = Frame(ventana)
    frame_tabla.pack(pady=10, fill=BOTH, expand=True)
    columnas = ["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"]
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla.heading(col, text=col)
        if col == "Fecha y hora":
            tabla.column(col, width=200, anchor=W)
        else:
            tabla.column(col, width=110, anchor=W)
    scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scroll_y.set)
    tabla.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")
    frame_tabla.grid_rowconfigure(0, weight=1)
    frame_tabla.grid_columnconfigure(0, weight=1)

    # --------------------------------------------------------------------------
    # BLOQUE NUEVO >>> funciones para limpiar y reacción al cambio de tipo
    # --------------------------------------------------------------------------
    def limpiar_tabla():
        """Vacía completamente la tabla Treeview."""
        for item in tabla.get_children():
            tabla.delete(item)

    def limpiar_campos():
        """Opcional: limpia las entradas de DNI y Fecha."""
        entry_dni.delete(0, END)
        entry_fecha.delete(0, END)

    def cambio_tipo_busqueda(*_):
        """Se ejecuta cuando cambias de DNI / Fecha / Ambos (por trace)."""
        limpiar_tabla()
        ultimos_registros.clear()
        # Si deseas limpiar campos cada vez que cambies tipo, descomenta:
        # limpiar_campos()
        # Opcional: enfocar el campo adecuado según el tipo seleccionado
        t = tipo_busqueda.get()
        if t == "dni":
            entry_dni.focus_set()
        elif t == "fecha":
            entry_fecha.focus_set()
        elif t == "ambos":
            entry_dni.focus_set()

    # Registrar el trace para detectar cambios de tipo_busqueda
    tipo_busqueda.trace_add("write", cambio_tipo_busqueda)

    # --------------------------------------------------------------------------
    # Mostrar/ocultar campos según tipo (actualiza la variable => dispara trace)
    # --------------------------------------------------------------------------
    def mostrar_campos(tipo: str):
        tipo_busqueda.set(tipo)  # <-- Esto dispara cambio_tipo_busqueda()
        # Limpiar entradas (independiente del trace)
        entry_dni.delete(0, END)
        entry_fecha.delete(0, END)
        # Quitar widgets actuales
        for w in (label_dni, entry_dni, label_fecha, entry_fecha):
            w.pack_forget()
        # Volver a mostrar según selección
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

    # Botones de selección de tipo ------------------------------------------------
    ttk.Button(
        frame_botones,
        text="Buscar por DNI",
        style="Green.TButton",
        width=20,
        command=lambda: mostrar_campos("dni"),
    ).grid(row=0, column=0, padx=5)

    ttk.Button(
        frame_botones,
        text="Buscar por Fecha",
        style="Blue.TButton",
        width=20,
        command=lambda: mostrar_campos("fecha"),
    ).grid(row=0, column=1, padx=5)

    ttk.Button(
        frame_botones,
        text="Buscar por DNI y Fecha",
        style="Red.TButton",
        width=25,
        command=lambda: mostrar_campos("ambos"),
    ).grid(row=0, column=2, padx=5)

    # --------------------------------------------------------------------------
    # Función principal de búsqueda
    # --------------------------------------------------------------------------
    def ejecutar_busqueda():
        # LIMPIAR SIEMPRE ANTES DE CARGAR NUEVOS RESULTADOS
        limpiar_tabla()

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

        # Actualizar buffer local
        ultimos_registros.clear()
        ultimos_registros.extend(registros)

        # Insertar resultados en la tabla
        if registros:
            for fila in registros:
                fila_c = list(fila)[:7] + [""] * (7 - len(fila))
                tabla.insert("", "end", values=fila_c[:7])
        else:
            messagebox.showinfo("Resultado", "🔎 No se encontraron asistencias.")

    # --------------------------------------------------------------------------
    # Generar PDF de la última búsqueda
    # --------------------------------------------------------------------------
    def generar_pdf():
        if not ultimos_registros:
            messagebox.showinfo("Sin datos", "No hay registros para exportar.")
            return
        sugerido = f"reporte_asistencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        ruta_pdf = filedialog.asksaveasfilename(
            title="Guardar reporte en PDF",
            defaultextension=".pdf",
            initialfile=sugerido,
            filetypes=[("PDF", "*.pdf"), ("Todos", "*.*")],
        )
        if not ruta_pdf:
            return
        try:
            exportar_asistencias_a_pdf(ultimos_registros, ruta_pdf)
            messagebox.showinfo("Éxito", f"PDF generado:\n{ruta_pdf}")
        except Exception as e:  # pragma: no cover - UI
            messagebox.showerror("Error", str(e))

    # Frame para los tres botones finales --------------------------------------
    frame_botones_final = Frame(ventana)
    frame_botones_final.pack(pady=15)

    ttk.Button(
        frame_botones_final,
        text="Buscar",
        style="Green.TButton",
        command=ejecutar_busqueda,
        width=18,
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        frame_botones_final,
        text="Generar PDF",
        style="Blue.TButton",
        command=generar_pdf,
        width=18,
    ).grid(row=0, column=1, padx=10)

    ttk.Button(
        frame_botones_final,
        text="Cerrar",
        style="Red.TButton",
        command=ventana.destroy,
        width=18,
    ).grid(row=0, column=2, padx=10)

    # Opcional: seleccionar "dni" al abrir para mostrar campos por defecto
    mostrar_campos("dni")
