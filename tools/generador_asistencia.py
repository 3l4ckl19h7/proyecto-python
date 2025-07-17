import csv
import random
from datetime import datetime, timedelta

# Lista de empleados simulados
empleados = [
    {"dni": "75210347", "nombres": "Carlos", "apellidos": "García"},
    {"dni": "80121322", "nombres": "Ana", "apellidos": "Pérez"},
    {"dni": "74549877", "nombres": "Luis", "apellidos": "Ramírez"},
    {"dni": "79810022", "nombres": "María", "apellidos": "Lozano"},
    {"dni": "70012345", "nombres": "Diana", "apellidos": "Cruz"},
    {"dni": "20251645", "nombres": "Jairo", "apellidos": "Macedo"},
    {"dni": "74549877", "nombres": "Juan", "apellidos": "Martínez"}
]

# Traducción de días al español con mayúscula y tilde
dias_traducidos = {
    "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles",
    "Thursday": "Jueves", "Friday": "Viernes"
}

def obtener_dias_laborales(base_fecha, rango_dias):
    """Devuelve lista de fechas laborales (lunes a viernes) dentro del rango."""
    dias = []
    for i in range(rango_dias + 1):
        dia = base_fecha + timedelta(days=i)
        if dia.weekday() < 5:  # 0: lunes, ..., 4: viernes
            dias.append(dia)
    return dias

def generar_historico_por_jornada(rango_dias, archivo_salida):
    """Genera registros por empleado y por día laboral, marcando presentes y ausentes."""
    base_fecha = datetime.now() - timedelta(days=rango_dias)
    dias_laborales = obtener_dias_laborales(base_fecha, rango_dias)

    with open(archivo_salida, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["DNI", "Apellidos", "Nombres", "Día", "Fecha y hora", "Tardanza", "Estado"])

        for fecha in dias_laborales:
            dia_en = fecha.strftime("%A")
            dia_es = dias_traducidos.get(dia_en, "-")
            fecha_simple = fecha.strftime("%d-%m-%Y")

            for emp in empleados:
                estado = "Presente" if random.random() > 0.15 else "Ausente"

                if estado == "Presente":
                    hora = random.randint(7, 10)
                    minuto = random.randint(0, 59)
                    fecha_completa = fecha.replace(hour=hora, minute=minuto)
                    fecha_hora = fecha_completa.strftime("%d-%m-%Y %H:%M:%S")
                    hora_base = datetime.strptime("08:00:00", "%H:%M:%S").time()
                    tardanza = "Sí" if fecha_completa.time() > hora_base else "No"
                else:
                    fecha_hora = f"{fecha_simple} -"
                    tardanza = "-"

                writer.writerow([
                    emp["dni"],
                    emp["apellidos"],
                    emp["nombres"],
                    dia_es,
                    fecha_hora,
                    tardanza,
                    estado
                ])

    print(f"✅ Se generaron {len(dias_laborales) * len(empleados)} registros completos en '{archivo_salida}'.")
