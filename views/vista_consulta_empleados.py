from modules.consulta_empleados import obtener_lista_empleados

def modulo_consulta_empleados():
    print("Modulo de consulta de empleados registrados")
    
    empleados = obtener_lista_empleados()

    archivo_csv = "data/Empleados.csv"

    if not os.path.isfile(archivo_csv):
        print("❌ No se encontró el archivo de empleados.")
        return
    
    
    with open(archivo_csv, "r", encoding= "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        empleados = list(lector)
        
        if not empleados:
            print("⚠️ No hay empleados registrados")
            return
        
        
        print(f"\n  Total de empleados: {len(empleados)}\n")
        print("{:<12} {:<20} {:<20} {:<10}".format("Codigo", "Apellidos", "Nombres", "Usuario", "Clave"))
        print("-" * 80)
        
        for emp in empleados:
            print("{:<12} {:<20} {:<20} {:<10}".format(
                emp['codigo'], emp['apellidos'], emp['nombres'], emp['usuario'], emp['clave']))
        
        print("-" * 80)