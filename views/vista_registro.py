# from utils.validaciones import validar_dni
# from modules.registra_asistencia import registrar_asistencia

# def mostrar_formulario_registro():
#     print("\n--- Registro de Asistencia ---")
#     while True:
#         dni = input("DNI: ")
#         if not validar_dni(dni):
#             print("❌ DNI inválido. Debe tener 8 dígitos numéricos.")
#         else:
#             print("✅ DNI válido.")
#             break

#     clave = input("Colocar clave: ")

#     # Aquí solo se envía el DNI y la clave para su validación en registra_asistencia.py
#     registrar_asistencia(dni, clave)
#     print("\n(La validación de la clave y el registro se realiza en el módulo correspondiente.)")
#     print("--- Fin del Registro ---\n")
    
from tkinter import *
from tkinter import messagebox
from utils.validaciones import validar_dni
from modules.registra_asistencia import registrar_asistencia

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

    # Función interna para validar y registrar
    def registrar():
        dni = entry_dni.get().strip()
        clave = entry_clave.get().strip()

        if not validar_dni(dni):
            messagebox.showerror("Error", "❌ DNI inválido. Debe tener 8 dígitos numéricos.")
            return

        registrar_asistencia(dni, clave)
        messagebox.showinfo("Registro Exitoso", "✅ Asistencia registrada correctamente.")
        ventana.destroy()

    Button(ventana, text="Registrar", bg="#4CAF50", fg="black", font=("Helvetica", 12, "bold"),
           width=15, command=registrar).pack(pady=15)

    Button(ventana, text="Cancelar", command=ventana.destroy).pack()

