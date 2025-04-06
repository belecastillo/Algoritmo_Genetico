
def exportar_resultados(datos, grupo1, mejor, ruta_csv='data/processed/resultado_datos.csv'):
    
    # Asignar grupo a cada individuo
    datos['Grupo'] = datos.index.to_series().apply(lambda x: 1 if x in mejor and x in grupo1 else 2)

    # Guardar en CSV
    datos.to_csv(ruta_csv, sep=',', index=True, encoding='utf-8')
    print(f"--> Resultados exportados a {ruta_csv}")