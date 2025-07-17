import csv
import os

def obtener_lista_empleados():
    archivo_csv = "data/Empleados.csv"

    if not os.path.isfile(archivo_csv):
        return None  # No existe el archivo

    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        empleados = list(lector)

        return empleados if empleados else []
    
    
    #Este es un comentario