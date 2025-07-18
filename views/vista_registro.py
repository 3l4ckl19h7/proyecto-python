from tkinter import *
from tkinter import ttk, messagebox
from utils.validaciones import validar_dni
from modules.registra_asistencia import registrar_asistencia, validar_datos_empleados

def mostrar_formulario_registro():
    ventana = Toplevel()
    ventana.title("Registro de Asistencia")
    ventana.geometry("350x250")
    ventana.resizable(False, False)

    # Centrar ventana
    ancho = 350
    alto = 250
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    Label(ventana, text="Registro de Asistencia", font=("Helvetica", 14, "bold")).pack(pady=10)

    # DNI
    Label(ventana, text="DNI:").pack()
    entry_dni = Entry(ventana, font=("Helvetica", 12))
    entry_dni.pack(pady=5)

    # Clave
    Label(ventana, text="Clave:").pack()
    entry_clave = Entry(ventana, font=("Helvetica", 12), show="*")
    entry_clave.pack(pady=5)

    # Estilos para colores (usar tema clam en macOS)
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Success.TButton", font=("Helvetica", 12, "bold"),
                    foreground="white", background="#4CAF50", padding=5)
    style.map("Success.TButton", background=[("active", "#66BB6A")])

    style.configure("Cancel.TButton", font=("Helvetica", 12, "bold"),
                    foreground="white", background="#C62828", padding=5)
    style.map("Cancel.TButton", background=[("active", "#E57373")])

    # Función interna para validar y registrar
    def registrar():
        dni = entry_dni.get().strip()
        clave = entry_clave.get().strip()

        if not validar_dni(dni):
            messagebox.showerror("Error", "❌ DNI inválido. Debe tener 8 dígitos numéricos.")
            return

        if not validar_datos_empleados(dni, clave):
            messagebox.showerror("Error", "❌ DNI o clave incorrectos, o usuario inactivo.")
            return

        resultado = registrar_asistencia(dni, clave)
        if resultado == "duplicado":
            messagebox.showwarning("Duplicado", "⚠️ Ya has registrado tu asistencia hoy.")
        elif resultado == "exito":
            messagebox.showinfo("Registro Exitoso", "✅ Asistencia registrada correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "❌ No se pudo registrar la asistencia.")

    # Botones con colores
    frame_btns = Frame(ventana)
    frame_btns.pack(pady=15)

    ttk.Button(frame_btns, text="Registrar", style="Success.TButton",
               command=registrar).pack(side=LEFT, padx=5)
    ttk.Button(frame_btns, text="Cancelar", style="Cancel.TButton",
               command=ventana.destroy).pack(side=LEFT, padx=5)
