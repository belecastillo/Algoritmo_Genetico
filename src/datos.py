import pandas as pd
from .utilidades import generar_lista_letras

ARCHIVO = 'data/raw/datos_generados.csv'

# Función para obtener los datos
def obtener_datos(ruta_csv=ARCHIVO):
    data = pd.read_csv(ruta_csv)
    data = generar_lista_letras(data)
    return data