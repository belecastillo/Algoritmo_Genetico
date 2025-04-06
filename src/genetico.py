import numpy as np
import random

# Función de distancia euclidiana
def distancia(punto1, punto2):
    return np.linalg.norm(np.array(punto1.astype(float)) - np.array(punto2.astype(float)))

# Evalua las aptitudes de los individuos
def evaluar_aptitud(individuo, data):
  """
    individuo: Lista con el grupo1 y grupo2 (combinacion)
    data: Dataframe con los datos de entrada para calcular la distancia
  """
  fitness = 0
  suma_distancia = 0
  n=int(len(individuo)/2)
  #Separar individuo en dos grupos.
  grupo1 = individuo[:n] # A B C D
  grupo2 = individuo[n:] # E F G H
  for i in range(n):
    # Acceda a los valores 'X' e 'Y' utilizando los nombres de columna apropiados, se recorre por las etiquetas (A, B, C...)
    punto1 = data.loc[grupo1[i], ['rating_consistent', 'rating_inconsistent','syllables','frequency']]
    punto2 = data.loc[grupo2[i], ['rating_consistent', 'rating_inconsistent','syllables','frequency']]
    suma_distancia += distancia(punto1, punto2) # Suma de las distancias de los pares de elementos
  fitness = (suma_distancia)/n # El fitness es el promedio de la distancia entre pares de elementos.
  return fitness # Un fitness más alto significa grupos más alejados entre sí (más heterogéneos)


# Función para seleccionar padres (Selección por Ruleta)
def seleccionar_padres(poblacion, aptitudes):
    # Invertir los valores de aptitud para favorecer individuos con menor distancia
    aptitud_total = sum(aptitudes)

    seleccion = random.uniform(0, aptitud_total) # Número aleatorio entre 0 y la suma total de aptitudes
    #print("Seleccion padre 1: ", seleccion)

    # Recorre la Población y acumula Aptitudes
    acumulado = 0
    for i, aptitud in enumerate(aptitudes): # Recorre la Población y acumula Aptitudes
        acumulado += aptitud # Va sumando las aptitudes
        if acumulado >= seleccion: # Hasta que el acumulado sea mayor o igual al nro de seleccion
            padre1 = poblacion[i]
            #print("Acumulado padre 1: ", acumulado)
            break

    padre2 = None
    # Se realiza el mismo procedimiento para el padre 2
    while padre2 is None:
        seleccion = random.uniform(0, aptitud_total)
        #print("Seleccion padre 2: ", seleccion)
        acumulado = 0
        for i, aptitud in enumerate(aptitudes):
          if poblacion[i] == padre1: # Si el padre 1 es igual al padre 2, 
            continue
          acumulado += aptitud
          if acumulado >= seleccion:
              padre2 = poblacion[i]
              #print("Acumulado padre 2: ", acumulado)
              break

    #print("Padre 1: ", padre1)
    #print("Padre 2: ", padre2)

    return padre1, padre2 #Se seleccionan dos padres de la población proporcionalmente a su aptitud


# CRUCE: Realiza el cruzamiento desde el punto de cruce
def cruzar(padre1, padre2):
    punto_cruce = random.randint(0, len(padre1)-2) # Elige un nro aleatorio entre 0 y la cantidad de elementos de padre1 - 1
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    #print("Hijo 1 cruzado: ", hijo1)
    #print("Hijo 2 cruzado: ", hijo2)
    #print("Punto de cruce: ", punto_cruce)
    return hijo1, hijo2


# Elegir posición a mutar
def mutacion_posicion(n, prob_mutacion):
    posicion = 1
    for i in range(n-1):
        if random.random() < prob_mutacion:
            posicion = i
            break
    return posicion

# MUTACION: Realiza la mutación de una posición aleatoria de individuos con una probabilidad dada.
def mutacion(hijo1, hijo2, data,prob_mutacion=0.3):
    # Crear una copia de los individuos para no modificar la lista original

    n = int(len(hijo1))

    p1 = mutacion_posicion(n, prob_mutacion)
    p2 = mutacion_posicion(n, prob_mutacion)

    l1 = hijo1[p1]
    l2 = hijo2[p2]

    #print("Se muta en la Posicion 1: ", p1+1, "->", l1)
    #print("Se muta en la Posicion 2: ", p2+1, "->", l2)

    # Se intercambian
    hijo1[p1] = l2
    hijo2[p2] = l1

    #print("Hijo mutado 1: ", hijo1)
    #print("Hijo mutado 2: ", hijo2)

    return hijo1, hijo2

# REPARACIÓN: Verifica que no se repitan los gen en un individuo, si se repiten, las cambia aleatoriamente a otra letra válida.
def verificar_y_corregir(individuo, data):
    letras_usadas = set()
    letras_validas = list(data.index)
    for i in range(len(individuo)):
        if individuo[i] in letras_usadas:
            # Encontrar una nueva letra válida que no esté en letras_usadas
            nueva_letra = random.choice([letra for letra in letras_validas if letra not in letras_usadas])
            individuo[i] = nueva_letra # Reemplaza por la nueva letra.
        letras_usadas.add(individuo[i])

    return individuo

# Elegir cual pasa a formar parte de la generación
def mejor_individuo(hijo1, hijo2, data):
  fitness_hijo1 = evaluar_aptitud(hijo1, data) # Calcula la aptutud del hijo 1
  fitness_hijo2 = evaluar_aptitud(hijo2, data) # Calcula la aptitud del hijo 2
  #print("Fitness hijo 1: ", fitness_hijo1)
  #print("Fitness hijo 2: ", fitness_hijo2)
  if fitness_hijo1 < fitness_hijo2: # Evalua cual fitness es mejor (para nuestro caso, el que tiene menor fitness) --> Estamos minimizando el fitness
    return hijo1
  else:
    return hijo2