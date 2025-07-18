from tkinter import *
from tkinter import messagebox

ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def mostrar_login(parent, callback_habilitar):
    login_win = Toplevel(parent)
    login_win.title("Login Administrador")

    # Tamaño ventana centrada
    ancho = 500
    alto =400
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (ancho // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (alto // 2)
    login_win.geometry(f"{ancho}x{alto}+{x}+{y}")
    login_win.resizable(False, False)

    # Fondo color para diferenciar (Mac)
    login_win.configure(bg="#F4F6F7")

    frame = Frame(login_win, bg="#F4F6F7", padx=20, pady=20)
    frame.pack(expand=True)

    Label(frame, text="Usuario:", bg="#F4F6F7", fg="#2C3E50", font=("Helvetica", 12)).pack(pady=5)
    entry_user = Entry(frame, font=("Helvetica", 12))
    entry_user.pack(pady=5)

    Label(frame, text="Contraseña:", bg="#F4F6F7", fg="#2C3E50", font=("Helvetica", 12)).pack(pady=5)
    entry_pass = Entry(frame, show="*", font=("Helvetica", 12))
    entry_pass.pack(pady=5)

    def validar():
        if entry_user.get() == ADMIN_USER and entry_pass.get() == ADMIN_PASS:
            messagebox.showinfo("Éxito", "Bienvenido Administrador")
            callback_habilitar()
            login_win.destroy()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    # Botón con color visible en Mac (usar tk.Button, no ttk)
    btn_ingresar = Button(frame, text="Ingresar", command=validar,
                          bg="#27AE60", fg="white", font=("Helvetica", 12, "bold"),
                          activebackground="#2ECC71", activeforeground="white",
                          relief="flat", padx=10, pady=5, cursor="hand2")
    btn_ingresar.pack(pady=10)
