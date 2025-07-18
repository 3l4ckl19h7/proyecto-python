from csv import writer
from os.path import join
from os import makedirs

def modulo_registro_empleados():
    print("\n📋 Registro de Empleados")

    ruta_archivo = join("data", "Empleados.csv")
    makedirs("data", exist_ok=True)

    while True:
        codigo = input("Código: ")
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        activo = input("¿Activo? (A/I): ").upper()
        if activo not in ["A", "I"]:
            activo = "A"

        # Asegurar salto de línea antes de escribir (si no existe)
        with open(ruta_archivo, "ab+") as archivo:
            archivo.seek(0, 2)  # Ir al final
            if archivo.tell() > 0:  # Si no está vacío
                archivo.seek(-1, 2)
                if archivo.read(1) != b"\n":
                    archivo.write(b"\n")

        # Agregar los datos al archivo CSV
        with open(ruta_archivo, mode="a", newline="", encoding="utf-8") as archivo:
            w = writer(archivo)
            w.writerow([codigo, apellido, nombre, usuario, clave, activo])

        print("✅ Empleado registrado con éxito.")

        otro = input("¿Registrar otro empleado? (s/n): ").lower()
        if otro != "s":
            break

