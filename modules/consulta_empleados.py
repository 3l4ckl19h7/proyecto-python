import csv
import os

def modulo_registro_empleados():
    print("\n=== Registro de Empleados ===")


    DNI = input("Ingrese el n° de Dni del empleado a registrar: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    nombres = input("Ingrese los nombres: ").strip()
    clave = input("Ingrese una clave de acceso de 4 digitos: ").strip()
    

    if len(DNI) != 8 or not DNI.isdigit():
        print("❌ DNI inválido. Debe tener 8 dígitos.")
        return
    
    if len(clave) != 4 or not clave.isdigit():
        print("❌ Clave inválida. Debe tener 4 dígitos.")
        return


# Generando el usuario del empleado

    iniciales_apellido = ''.join([x[0] for x in apellidos.split() if x])  
    iniciales_nombre = ''.join([x[0] for x in nombres.split() if x])
    usuario = (iniciales_nombre) + (iniciales_apellido).upper()


    archivo_csv = "data/Empleados.csv" #Consultar ruta del csv 
    archivo_existe = os.path.isfile(archivo_csv)
    
    
    with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        
        
        if not archivo_existe or os.path.getsize(archivo_csv) == 0:
            writer.writerow(["DNI", "apellidos", "nombres", "usuario", "clave",])
            
        writer.writerow([DNI, apellidos, nombres, usuario, clave])

    print(f"✅ Empleado {nombres} {apellidos} registrado correctamente con usuario '{usuario} '.")





