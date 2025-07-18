# from modules.consulta_empleados import obtener_lista_empleados

# def modulo_consulta_empleados():
#     print("Modulo de consulta de empleados registrados")
    
#     empleados = obtener_lista_empleados()
    
#     if empleados is None:
#         print("❌ No se encontró el archivo de empleados.")
#         return
#     elif not empleados:
#         print("⚠️ No hay empleados registrados")
        
        
               
#         print(f"\n  Total de empleados: {len(empleados)}\n")
#         print("{:<12} {:<20} {:<20} {:<10}".format("Codigo", "Apellidos", "Nombres", "Usuario", "Clave"))
#         print("-" * 80)
        
#         for emp in empleados:
#             print("{:<12} {:<20} {:<20} {:<10}".format(
#                 emp['codigo'], emp['apellidos'], emp['nombres'], emp['usuario'], emp['clave']))
        
#         print("-" * 80)
        
        
        #Este tambien 

from tkinter import *
from tkinter import ttk, messagebox
from modules.consulta_empleados import obtener_lista_empleados

def modulo_consulta_empleados():
    # Obtener lista de empleados
    empleados = obtener_lista_empleados()

    if empleados is None:
        messagebox.showerror("Error", "No se encontró el archivo 'Empleados.csv'.")
        return
    if not empleados:
        messagebox.showwarning("Aviso", "No hay empleados registrados.")
        return

    # Crear ventana principal
    ventana = Toplevel()
    ventana.title("Lista de Empleados")
    ventana.configure(bg="#F8F9F9")

    # Calcular tamaño y centrar ventana
    ancho_ventana = 1000
    alto_ventana = 600
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho_ventana // 2)
    y = (pantalla_alto // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.grab_set()

    # Título
    Label(ventana, text="Lista de Empleados",
          font=("Helvetica", 18, "bold"), bg="#F8F9F9", fg="#2C3E50").pack(pady=(15, 5))

    Label(ventana, text=f"Total de empleados: {len(empleados)}",
          font=("Helvetica", 12), bg="#F8F9F9", fg="#555555").pack(pady=(0, 10))

    # Contenedor para la tabla
    cont_tabla = Frame(ventana, bg="#F8F9F9")
    cont_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Columnas reales
    columnas = ["código", "apellido", "nombre", "usuario", "clave", "activo"]
    tabla = ttk.Treeview(cont_tabla, columns=columnas, show="headings", height=15)

    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        ancho = 120 if col != "clave" else 150
        tabla.column(col, width=ancho, anchor=W)

    # Scrollbars
    scroll_y = ttk.Scrollbar(cont_tabla, orient=VERTICAL, command=tabla.yview)
    scroll_x = ttk.Scrollbar(cont_tabla, orient=HORIZONTAL, command=tabla.xview)
    tabla.configure(yscroll=scroll_y.set, xscroll=scroll_x.set)

    tabla.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")
    scroll_x.grid(row=1, column=0, sticky="ew")
    cont_tabla.grid_rowconfigure(0, weight=1)
    cont_tabla.grid_columnconfigure(0, weight=1)

    # Insertar datos en la tabla con clave oculta
    for emp in empleados:
        clave_oculta = "*" * len(emp.get("clave", ""))  # Asteriscos en lugar de clave real
        fila = [emp.get("código", ""), emp.get("apellido", ""), emp.get("nombre", ""),
                emp.get("usuario", ""), clave_oculta, emp.get("activo", "")]
        tabla.insert("", "end", values=fila)

    # Botón cerrar
    Button(ventana, text="Cerrar", command=ventana.destroy,
           bg="#C0392B", fg="white", font=("Helvetica", 12, "bold"), width=15).pack(pady=10)
