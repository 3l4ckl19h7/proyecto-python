import csv
import os

print(os.listdir())

# Ruta al archivo CSV
ruta_archivo = 'D:\\Develop\\blmcs-python\\Proyecto\\Empleados.csv'

try:
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        print("Listado de usuarios:\n")
        for fila in lector:
            print(f"Código: {fila['código']}")
            print(f"Apellido: {fila['apellido']}")
            print(f"Nombre: {fila['nombre']}")
            print(f"Usuario: {fila['usuario']}")
            print(f"Clave: {fila['clave']}")
            print(f"Activo: {fila['activo']}\n")
            print("-" * 40)

except FileNotFoundError:
    print(f"No se encontró el archivo '{ruta_archivo}'.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
