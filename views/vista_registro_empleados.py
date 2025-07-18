import tkinter as tk
from tkinter import ttk, messagebox
from csv import writer
from os.path import join, exists
from os import makedirs

def modulo_registro_empleados():
    # Crear ventana emergente
    ventana = tk.Toplevel()
    ventana.title("Registro de Empleados")
    ventana.resizable(False, False)

    # Dimensiones y centrado
    ancho, alto = 400, 400
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # Crear carpeta y archivo
    ruta_archivo = join("data", "Empleados.csv")
    makedirs("data", exist_ok=True)

    # Cambiar theme para personalización en macOS
    style = ttk.Style()
    style.theme_use("clam")

    # Estilos
    style.configure("Custom.TFrame", background="#f0f0f0")
    style.configure("Custom.TLabel", background="#f0f0f0", font=("Arial", 11))
    style.configure("Custom.TEntry", fieldbackground="white", foreground="#333", padding=5)
    style.configure("Custom.TButton",
                    font=("Arial", 11, "bold"),
                    background="#4CAF50",
                    foreground="white",
                    padding=6)
    style.map("Custom.TButton",
              background=[("active", "#45a049")],
              foreground=[("active", "white")])

    # Contenedor principal
    contenedor = ttk.Frame(ventana, style="Custom.TFrame", padding=20)
    contenedor.pack(fill="both", expand=True)

    # Etiquetas y campos
    labels = ["Código", "Apellido", "Nombre", "Usuario", "Clave", "Activo (A/I)"]
    entries = {}

    for i, label in enumerate(labels):
        ttk.Label(contenedor, text=label + ":", style="Custom.TLabel").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = ttk.Entry(contenedor, style="Custom.TEntry", show="*" if label == "Clave" else "")
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    # Función para guardar empleado
    def guardar_empleado():
        codigo = entries["Código"].get().strip()
        apellido = entries["Apellido"].get().strip()
        nombre = entries["Nombre"].get().strip()
        usuario = entries["Usuario"].get().strip()
        clave = entries["Clave"].get().strip()
        activo = entries["Activo (A/I)"].get().strip().upper()

        if not all([codigo, apellido, nombre, usuario, clave]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if activo not in ["A", "I"]:
            activo = "A"

        # Crear encabezado si archivo no existe o está vacío
        nuevo_archivo = not exists(ruta_archivo) or (exists(ruta_archivo) and open(ruta_archivo).read().strip() == "")

        with open(ruta_archivo, mode="a", newline="", encoding="utf-8") as archivo:
            w = writer(archivo)
            if nuevo_archivo:
                w.writerow(labels)  # Encabezado
            w.writerow([codigo, apellido, nombre, usuario, clave, activo])

        messagebox.showinfo("Éxito", "Empleado registrado con éxito.")

        for entry in entries.values():
            entry.delete(0, tk.END)

    # Botón Guardar
    btn_guardar = ttk.Button(contenedor, text="Registrar Empleado", style="Custom.TButton", command=guardar_empleado)
    btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=20)

    ventana.mainloop()

