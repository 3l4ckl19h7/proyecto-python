from datetime import datetime
from utils.validaciones import validar_dni

def registrar_asistencia(DNI):

    ahora = datetime.now()
    sin_milisegundos = ahora.strftime("%Y-%m-%d %H:%M:%S")

    if validar_dni(DNI):
        pass
    else:
        print("DNI inválido. Debe tener 8 dígitos.")




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


