from .genetico import evaluar_aptitud, seleccionar_padres, cruzar, mutacion, verificar_y_corregir, mejor_individuo

# Lógica del algoritmo: selección, cruce, mutación, evaluación, etc.
# Llamás a todas tus otras funciones dentro de acá
def algoritmo_genetico(data, num_generaciones, tam_poblacion, tasa_mutacion, poblacion):
    #print("Inicio del algoritmo genético")
    generaciones = []
    for _ in range(num_generaciones): #Itera hasta llegar a la cantidad de generaciones definidas
        #print("Generación: ", _)
        aptitudes = [evaluar_aptitud(individuo, data) for individuo in poblacion] #Evalua la aptitud de cada grupo de individuos de la poblacion válida.(Toma las combinaciones)
        nueva_poblacion = []
        while len(nueva_poblacion) < tam_poblacion:
            padre1, padre2 = seleccionar_padres(poblacion, aptitudes) # Selección de padres
            hijo1, hijo2 = cruzar(padre1, padre2) # cruce de padres
            hijo1_mutado, hijo2_mutado = mutacion(list(hijo1), list(hijo2), data, tasa_mutacion)
            hijo1_mutado = verificar_y_corregir(hijo1_mutado, data) # Se verifica que no hay gen repetido
            hijo2_mutado = verificar_y_corregir(hijo2_mutado, data)
            #print("Hijo mutado verificado 1: ", hijo1_mutado)
            #print("Hijo mutado verificado 2: ", hijo2_mutado)
            mejor_hijo = mejor_individuo(hijo1_mutado, hijo2_mutado, data) # se selecciona al mejor individuo, el que tiene menor fitness
            nueva_poblacion.extend([mejor_hijo]) # Se agrega a la nueva población
            #print("Nueva poblacion: ", nueva_poblacion)
        mejor_de_la_generacion = min(nueva_poblacion, key=lambda ind: evaluar_aptitud(ind, data)) # De la nueva problación, se elige el individuo con menor fitness.
        generaciones.append(mejor_de_la_generacion) # Se agrega a la generación
        poblacion = nueva_poblacion[:tam_poblacion]  # Asegurar que la población no exceda el tamaño --> Esta es la nueva poblacion
    # Seleccionar el individuo con la menor distancia promedio (mínimo fitness) de la generación
    mejor_ind = min(generaciones, key=lambda ind: evaluar_aptitud(ind, data))
    fitness = [evaluar_aptitud(individuo, data) for individuo in generaciones]
    imprimir_resultados(generaciones, fitness)
    print("El mejor Fitness: ", evaluar_aptitud(mejor_ind, data))
    return mejor_ind

def imprimir_resultados(generaciones, fitness):
  print("Los mejores de las Generaciones: ")
  for i,j in zip(generaciones,fitness):
    print(i, "Fitness: ", j)