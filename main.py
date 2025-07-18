from views.menu_principal import mostrar_menu
from tools.generador_asistencia import generar_historico_por_jornada

generar_historico_por_jornada(30, "data/historico_asistencias.csv")

if __name__ == "__main__":
    mostrar_menu()
