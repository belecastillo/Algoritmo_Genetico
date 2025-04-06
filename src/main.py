from .datos import obtener_datos
from .utilidades import generar_poblacion_valida
from .algoritmo import algoritmo_genetico
from .exportar import exportar_resultados
from .graficos import graficar_resultado

def main():
    print('***Algoritmo genético iniciado***')

    # Cargar los datos
    datos = obtener_datos()
    print("Datos cargados:")
    print(datos.head())

    # Inicializar parámetros 
    num_generaciones = 20
    tam_poblacion = 20
    tasa_mutacion = 0.1

    #Generamos una población válida que será la población inicial
    poblacion_va = generar_poblacion_valida(datos, tam_poblacion)

    # Ejecutar el algoritmo genético
    mejor = algoritmo_genetico(datos, num_generaciones, tam_poblacion, tasa_mutacion, poblacion_va)
    c = int(len(mejor)/2)
    grupo1 = mejor[:c]
    grupo2 = mejor[c:]
    print("Grupo 1: ", grupo1)
    print("Grupo 2: ", grupo2)

    # Graficar los resultados
    graficar_resultado(datos, grupo1, grupo2)

    #Exportar resultados en un archivo csv.
    exportar_resultados(datos, grupo1, mejor)

    print('***Algoritmo genético finalizado***')


if __name__ == '__main__':
    main()