import csv
from typing import List
from datetime import datetime

def ordenar_por_fecha(registros: List[List[str]]) -> List[List[str]]:
    """Ordena los registros por la fecha laboral, presente o ausente."""
    try:
        return sorted(
            registros,
            key=lambda fila: datetime.strptime(fila[4].split()[0], "%d-%m-%Y"),
            reverse=True
        )
    except (IndexError, ValueError):
        return registros

def obtener_asistencia_por_usuario(dni: str):
    asistencias = []
    try:
        with open("data/historico_asistencias.csv", mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            for fila in reader:
                if len(fila) > 4 and fila[0] == dni:
                    asistencias.append(fila)
    except FileNotFoundError:
        print("⚠️ Archivo de asistencia no encontrado.")
    return ordenar_por_fecha(asistencias)

def obtener_asistencia_por_fecha(fecha: str) -> List[List[str]]:
    asistencias = []
    try:
        with open("data/historico_asistencias.csv", mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            for fila in reader:
                if len(fila) > 4 and fecha in fila[4]:
                    asistencias.append(fila)
    except FileNotFoundError:
        print("⚠️ Archivo de asistencia no encontrado.")
    return ordenar_por_fecha(asistencias)

def obtener_asistencia_por_dni_y_fecha(dni: str, fecha: str) -> List[List[str]]:
    asistencias = []
    try:
        with open("data/historico_asistencias.csv", mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            for fila in reader:
                if len(fila) > 4 and fila[0] == dni and fecha in fila[4]:
                    asistencias.append(fila)
    except FileNotFoundError:
        print("⚠️ Archivo de asistencia no encontrado.")
    return ordenar_por_fecha(asistencias)
