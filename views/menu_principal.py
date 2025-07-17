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
#from PIL import Image, ImageTk
from views.vista_registro import mostrar_formulario_registro
from views.vista_consulta import mostrar_consulta
from views.vista_registro_empleados import modulo_registro_empleados
from pathlib import Path

def mostrar_menu():
    ventana = Tk()
    ventana.title("Menú Principal")

    # Tamaño ventana
    ancho = 1000
    alto = 600
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana.resizable(False, False)

    # --- Encabezado (ocupa todo el ancho) ---
    header = Frame(ventana, bg="#34495E", height=80)
    header.pack(fill=X)
    Label(header, text="SISTEMA DE CONTROL DE ASISTENCIA",
          fg="white", bg="#34495E", font=("Helvetica", 26, "bold")).pack(pady=20)

    # --- Frame principal que contiene dos columnas ---
    frame_main = Frame(ventana)
    frame_main.pack(fill=BOTH, expand=True)

    # --- Columna izquierda (imagen) ---
    frame_izq = Frame(frame_main, width=ancho // 2, height=alto - 80)
    frame_izq.pack(side=LEFT, fill=Y)

    # Cargar imagen
    base_dir = Path(__file__).resolve().parents[1]
    ruta_fondo = base_dir / "assets" / "fondo2.png"

    fondo_imgtk = None
    # if ruta_fondo.exists():
    #     try:
    #         #from PIL import Image
    #         img = Image.open(ruta_fondo)
    #         img = img.resize((ancho // 2, alto - 80), Image.LANCZOS)
    #         fondo_imgtk = ImageTk.PhotoImage(img, master=ventana)
    #     except Exception as e:
    #         print("Error cargando imagen:", e)

    if fondo_imgtk:
        Label(frame_izq, image=fondo_imgtk).pack(fill=BOTH, expand=True)
    else:
        frame_izq.configure(bg="#BDC3C7")

    # --- Columna derecha (menú) ---
    frame_der = Frame(frame_main, bg="#FFFFFF", width=ancho // 2)
    frame_der.pack(side=RIGHT, fill=BOTH, expand=True)

    Label(frame_der, text="Menú Principal", font=("Helvetica", 24, "bold"),
          bg="#FFFFFF", fg="#2C3E50").pack(pady=30)

    # Botones
    style_btn = {
        "width": 30, "height": 2,
        "font": ("Helvetica", 14, "bold"),
        "fg": "black", "relief": "flat", "bd": 0
    }

    Button(frame_der, text="Registrar asistencia",
           bg="#27AE60", command=mostrar_formulario_registro, **style_btn).pack(pady=15)
    Button(frame_der, text="Consultar asistencia",
           bg="#2980B9", command=mostrar_consulta, **style_btn).pack(pady=15)
    Button(frame_der, text="Registrar empleados",
           bg="#8E44AD", command=modulo_registro_empleados, **style_btn).pack(pady=15)
    Button(frame_der, text="Consultar empleados",
           bg="#8E44AD", command=modulo_consulta_empleados, **style_btn).pack(pady=15)
    Button(frame_der, text="Salir",
           bg="#C0392B", command=ventana.destroy, **style_btn).pack(pady=30)

    ventana.mainloop()
