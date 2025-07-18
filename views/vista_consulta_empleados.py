from tkinter import *
from tkinter import ttk, messagebox, filedialog
from modules.consulta_empleados import obtener_lista_empleados, buscar_empleado_por_codigo
from datetime import datetime
import os

# Función para generar PDF
def exportar_empleados_a_pdf(registros, ruta_pdf: str, titulo: str = "Lista de Empleados"):
    if not registros:
        raise ValueError("No hay registros para exportar.")

    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors
        from reportlab.platypus import Table, TableStyle
    except ImportError:
        raise ImportError("Instala reportlab: pip install reportlab")

    # Datos para la tabla
    columnas = ["Código", "Apellido", "Nombre", "Usuario", "Clave", "Activo"]
    filas = []
    for emp in registros:
        clave = emp.get("clave", "")
        clave_oculta = "*" * len(clave) if clave else ""
        filas.append([
            emp.get("código", ""),
            emp.get("apellido", ""),
            emp.get("nombre", ""),
            emp.get("usuario", ""),
            clave_oculta,
            emp.get("activo", ""),
        ])

    # Configuración de página
    page_size = landscape(A4)
    ancho_pag, alto_pag = page_size
    margin_x, margin_y = 40, 40
    espacio_top, espacio_bottom = 80, 40
    col_widths = [80, 140, 140, 140, 100, 60]
    row_height = 20

    c = canvas.Canvas(ruta_pdf, pagesize=page_size)
    generado = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    total = f"Total: {len(filas)}"
    usable_height = alto_pag - espacio_top - espacio_bottom
    filas_por_pagina = max(1, int(usable_height // row_height))

    def dibujar_encabezado(pagina_num, num_paginas):
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.HexColor("#2C3E50"))
        c.drawString(margin_x, alto_pag - margin_y, titulo)

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.black)
        c.drawString(margin_x, alto_pag - margin_y - 18, total)
        c.drawString(margin_x, alto_pag - margin_y - 32, f"Generado: {generado}")
        c.drawRightString(ancho_pag - margin_x, alto_pag - margin_y - 18, f"Página {pagina_num}/{num_paginas}")

        # Línea separadora
        c.setStrokeColor(colors.HexColor("#D5D8DC"))
        c.setLineWidth(0.5)
        c.line(margin_x, alto_pag - margin_y - 40, ancho_pag - margin_x, alto_pag - margin_y - 40)

    def dibujar_pagina(subfilas, pagina_num, num_paginas):
        dibujar_encabezado(pagina_num, num_paginas)
        page_data = [columnas] + subfilas
        t = Table(page_data, colWidths=col_widths, rowHeights=row_height)
        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#34495E")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8F9F9")]),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ])
        t.setStyle(style)
        top_y = alto_pag - espacio_top
        y = top_y - (row_height * len(page_data))
        if y < margin_y:
            y = margin_y
        t.wrapOn(c, ancho_pag - margin_x * 2, usable_height)
        t.drawOn(c, margin_x, y)
        c.showPage()

    sublistas = [filas[i:i + filas_por_pagina] for i in range(0, len(filas), filas_por_pagina)]
    num_paginas = len(sublistas)
    for idx, subfilas in enumerate(sublistas, start=1):
        dibujar_pagina(subfilas, idx, num_paginas)

    c.save()


def modulo_consulta_empleados():
    empleados = obtener_lista_empleados()
    if empleados is None:
        messagebox.showerror("Error", "No se encontró el archivo 'Empleados.csv'.")
        return
    if not empleados:
        messagebox.showwarning("Aviso", "No hay empleados registrados.")
        return

    ultimos_empleados_mostrados = list(empleados)

    ventana = Toplevel()
    ventana.title("Lista de Empleados")

    ancho_ventana, alto_ventana = 1000, 700
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.grab_set()

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"), foreground="#FFFFFF", background="#34495E")
    style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    style.configure("Primary.TButton", background="#2980B9", foreground="white", font=("Helvetica", 11, "bold"))
    style.configure("Danger.TButton", background="#C0392B", foreground="white", font=("Helvetica", 11, "bold"))
    style.configure("Success.TButton", background="#27AE60", foreground="white", font=("Helvetica", 11, "bold"))

    frame = ttk.Frame(ventana)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    ttk.Label(frame, text="Lista de Empleados", font=("Helvetica", 18, "bold")).pack(pady=(15, 5))
    lbl_total = ttk.Label(frame, text=f"Total de empleados: {len(empleados)}", font=("Helvetica", 12))
    lbl_total.pack(pady=(0, 10))

    frame_busqueda = ttk.Frame(frame)
    frame_busqueda.pack(fill=X, padx=10, pady=(0, 10), anchor="e")

    ttk.Label(frame_busqueda, text="Buscar por Código:").pack(side=LEFT, padx=5)
    entry_busqueda = ttk.Entry(frame_busqueda, width=20)
    entry_busqueda.pack(side=LEFT, padx=5)

    cont_tabla = ttk.Frame(frame)
    cont_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

    columnas = ["código", "apellido", "nombre", "usuario", "clave", "activo"]
    tabla = ttk.Treeview(cont_tabla, columns=columnas, show="headings", height=15)

    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        ancho = 120 if col != "clave" else 150
        tabla.column(col, width=ancho, anchor=W)

    scroll_y = ttk.Scrollbar(cont_tabla, orient=VERTICAL, command=tabla.yview)
    scroll_x = ttk.Scrollbar(cont_tabla, orient=HORIZONTAL, command=tabla.xview)
    tabla.configure(yscroll=scroll_y.set, xscroll=scroll_x.set)
    tabla.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")
    scroll_x.grid(row=1, column=0, sticky="ew")
    cont_tabla.grid_rowconfigure(0, weight=1)
    cont_tabla.grid_columnconfigure(0, weight=1)

    def limpiar_tabla():
        for item in tabla.get_children():
            tabla.delete(item)

    def mostrar_empleados(lista):
        limpiar_tabla()
        for emp in lista:
            clave_oculta = "*" * len(emp.get("clave", ""))
            fila = [emp.get("código", ""), emp.get("apellido", ""), emp.get("nombre", ""),
                    emp.get("usuario", ""), clave_oculta, emp.get("activo", "")]
            tabla.insert("", "end", values=fila)
        lbl_total.config(text=f"Mostrando: {len(lista)} / Total: {len(empleados)}")
        ultimos_empleados_mostrados.clear()
        ultimos_empleados_mostrados.extend(lista)

    def buscar():
        codigo = entry_busqueda.get().strip()
        if not codigo:
            messagebox.showinfo("Aviso", "Ingrese un código para buscar.")
            return
        resultado = buscar_empleado_por_codigo(codigo)
        if resultado:
            mostrar_empleados([resultado])
        else:
            messagebox.showinfo("Sin resultados", f"No se encontró el código {codigo}.")

    def restaurar():
        entry_busqueda.delete(0, END)
        mostrar_empleados(empleados)

    def generar_pdf():
        if not ultimos_empleados_mostrados:
            messagebox.showinfo("Sin datos", "No hay registros para exportar.")
            return
        sugerido = f"reporte_empleados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        ruta_pdf = filedialog.asksaveasfilename(
            title="Guardar reporte en PDF",
            defaultextension=".pdf",
            initialfile=sugerido,
            filetypes=[("PDF", "*.pdf"), ("Todos", "*.*")],
        )
        if not ruta_pdf:
            return
        try:
            exportar_empleados_a_pdf(ultimos_empleados_mostrados, ruta_pdf)
            messagebox.showinfo("Éxito", f"PDF generado:\n{ruta_pdf}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(frame_busqueda, text="Buscar", style="Primary.TButton", command=buscar).pack(side=LEFT, padx=5)
    ttk.Button(frame_busqueda, text="Limpiar", style="Danger.TButton", command=restaurar).pack(side=LEFT, padx=5)

    frame_botones = ttk.Frame(frame)
    frame_botones.pack(pady=10)
    ttk.Button(frame_botones, text="Generar Reporte", style="Success.TButton", command=generar_pdf).grid(row=0, column=0, padx=10)
    ttk.Button(frame_botones, text="Cerrar", style="Danger.TButton", command=ventana.destroy).grid(row=0, column=1, padx=10)

    mostrar_empleados(empleados)
