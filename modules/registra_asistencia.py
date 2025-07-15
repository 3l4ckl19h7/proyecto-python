from datetime import datetime
from utils.validaciones import validar_dni
import csv
import os

def get_data_path(filename: str) -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'data', filename)

def registrar_asistencia(DNI, clave):
    # Validar DNI
    if not validar_dni(DNI):
        print("❌ DNI inválido. Debe tener 8 dígitos.")
        return

    empleados_path = get_data_path('Empleados.csv')
    historico_path = get_data_path('historico_asistencias.csv')

    empleado = None
    with open(empleados_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['código'] == DNI and row['clave'] == clave and (row.get('activo', 'A') == 'A' or row.get('activo', '') == ''):
                empleado = row
                break

    if not empleado:
        print("❌ DNI o clave incorrectos, o usuario inactivo.")
        return

    # Datos para el registro
    ahora = datetime.now()
    dia_semana = ahora.strftime("%A")
    dias_es = {
        "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles",
        "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"
    }
    dia_semana = dias_es.get(dia_semana, dia_semana)
    fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")

    # Determinar tardanza (ejemplo: después de las 08:00:00 es tardanza)
    hora_limite = ahora.replace(hour=8, minute=0, second=0, microsecond=0)
    tardanza = "Sí" if ahora > hora_limite else "No"

    # Guardar registro en historico_asistencias.csv
    with open(historico_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            DNI,
            empleado['apellido'],
            empleado['nombre'],
            dia_semana,
            fecha_hora,
            tardanza,
            "Presente"
        ])
    print(f"✅ Asistencia registrada correctamente. ¡Bienvenido/a {empleado['nombre']} {empleado['apellido']}!")


def validar_hora_entrada(hora_entrada):
    # Aquí podrías implementar una lógica para validar la hora de entrada
    # Por simplicidad, asumiremos que la hora de entrada es válida si está en formato HH:MM
    try:
        datetime.strptime(hora_entrada, "%H:%M")
        return True
    except ValueError:
        return False

def validar_registro_asistencia(dni, hora_entrada):
    pass

