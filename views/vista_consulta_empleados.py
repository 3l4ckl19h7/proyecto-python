from modules.consulta_empleados import obtener_lista_empleados

def modulo_consulta_empleados():
    print("Modulo de consulta de empleados registrados")
    
    empleados = obtener_lista_empleados()
    
    if empleados is None:
        print("❌ No se encontró el archivo de empleados.")
        return
    elif not empleados:
        print("⚠️ No hay empleados registrados")
        
        
               
        print(f"\n  Total de empleados: {len(empleados)}\n")
        print("{:<12} {:<20} {:<20} {:<10}".format("Codigo", "Apellidos", "Nombres", "Usuario", "Clave"))
        print("-" * 80)
        
        for emp in empleados:
            print("{:<12} {:<20} {:<20} {:<10}".format(
                emp['codigo'], emp['apellidos'], emp['nombres'], emp['usuario'], emp['clave']))
        
        print("-" * 80)
        
        
        #Este tambien 