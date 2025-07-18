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


def buscar_empleado_por_codigo(codigo):
    empleados = obtener_lista_empleados()
    if empleados is None:
        return None
    
    
    for emp in empleados:
        if emp.get("código") == codigo:
             return emp
    
    return {}