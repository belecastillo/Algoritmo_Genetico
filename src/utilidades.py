import random
import string

# Generar una lista de letras del abecedario según la cantidad de datos
def generar_lista_letras(data):
    cantidad = data.shape[0]  # Obtiene la cantidad de filas en el DataFrame
    letras = list(string.ascii_uppercase)  # Genera las letras de A a Z
    resultado = []
    # Función auxiliar para generar combinaciones de longitud variable
    def generar_combinacion(n):
        combinacion = []
        while n >= 0:
            combinacion.append(letras[n % len(letras)])
            n = n // len(letras) - 1
        return ''.join(combinacion[::-1])  # Combina y devuelve la lista al revés para obtener la letra correcta
    i = 0
    while len(resultado) < cantidad:
        resultado.append(generar_combinacion(i))
        i += 1
    data.index = resultado[:cantidad] #Se agrega las letras en el indice del dataframe
    return data  # Retorna solo la cantidad de letras solicitadas


#Función para generar una población válida
def generar_poblacion_valida(data, tam_poblacion):
    individuos = list(data.index)
    n = int(len(individuos) / 2)
    combinaciones_unicas = set()
    soluciones = []
    poblacion = []
    while len(poblacion) < tam_poblacion:
        random.seed()  # Esto establece la semilla a partir del reloj del sistema
        # Mezcla aleatoria de los individuos
        random.shuffle(individuos)
        grupo1 = frozenset(individuos[:n])
        grupo2 = frozenset(individuos[n:])
        # Solo añadir si la combinación de grupos no está ya en el conjunto
        if (grupo1, grupo2) not in combinaciones_unicas and (grupo2, grupo1) not in combinaciones_unicas:
            combinaciones_unicas.add((grupo1, grupo2))
            soluciones.append(list(grupo1) + list(grupo2))
            #print("Combibaciones unicas: Grupo 1: ", grupo1, " Grupo 2: ", grupo2)
            poblacion.append(individuos[:])  # Copia la lista actual de individuos
    return soluciones #combinaciones_unicas