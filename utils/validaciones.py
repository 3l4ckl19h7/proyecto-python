from datetime import datetime

def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()

def validar_fecha(fecha_str):
    """Valida que una fecha esté en formato DD-MM-YYYY y sea una fecha real."""
    try:
        datetime.strptime(fecha_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
