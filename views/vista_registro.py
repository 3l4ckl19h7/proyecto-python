from utils.validaciones import validar_dni
from modules.registra_asistencia import registrar_asistencia

def mostrar_formulario_registro():
    print("\n--- Registro de Asistencia ---")
    while True:
        dni = input("DNI: ")
        if not validar_dni(dni):
            print("❌ DNI inválido. Debe tener 8 dígitos numéricos.")
        else:
            print("✅ DNI válido.")
            break

    clave = input("Colocar clave: ")

    # Aquí solo se envía el DNI y la clave para su validación en registra_asistencia.py
    registrar_asistencia(dni, clave)
    print("\n(La validación de la clave y el registro se realiza en el módulo correspondiente.)")
    print("--- Fin del Registro ---\n")
    