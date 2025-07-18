from datetime import datetime
from utils.validaciones import validar_dni
import csv
import os

def get_data_path(filename: str) -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'data', filename)

def validar_dni_empleado(DNI):
    if not validar_dni(DNI):
        print("❌ DNI inválido. Debe tener 8 dígitos.")
        return False
    empleados_path = get_data_path('Empleados.csv')
    with open(empleados_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['código'] == DNI and (row.get('activo', 'A') == 'A' or row.get('activo', '') == ''):
                return row
    print("❌ DNI incorrecto o usuario inactivo.")
    return False

def validar_clave_empleado(empleado, clave):
    if empleado and empleado['clave'] == clave:
        return True
    print("❌ Clave incorrecta.")
    return False

def asistencia_ya_registrada(DNI, fecha):
    historico_path = get_data_path('historico_asistencias.csv')
    if not os.path.exists(historico_path):
        return False
    with open(historico_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and row[0] == DNI and row[4][:10] == fecha:
                return True
    return False

def registrar_asistencia(DNI, clave):
    empleado = validar_dni_empleado(DNI)
    if not empleado:
        return

    if not validar_clave_empleado(empleado, clave):
        return

    historico_path = get_data_path('historico_asistencias.csv')

    ahora = datetime.now()
    dia_semana = ahora.strftime("%A")
    dias_es = {
        "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles",
        "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"
    }
    dia_semana = dias_es.get(dia_semana, dia_semana)
    fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
    fecha_actual = ahora.strftime("%d-%m-%Y")

    # Validar si ya registró asistencia hoy
    if asistencia_ya_registrada(DNI, fecha_actual):
        print("⚠️ Ya has registrado tu asistencia hoy.")
        return

    hora_limite = ahora.replace(hour=8, minute=0, second=0, microsecond=0)
    tardanza = "Sí" if ahora > hora_limite else "No"

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

