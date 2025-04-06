from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def graficar_resultado(data, grupo1, grupo2, ruta_guardado='outputs/figuras/grafico_resultados.png'):
    """
    Función para graficar el resultado del algoritmo genético.

    mejor_individuo: Lista con los dos grupos de individuos.
    data: DataFrame con los datos originales.
    """

    df = data
    df_grupo1 = df.loc[grupo1]
    df_grupo2 = df.loc[grupo2]


    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(df_grupo1['rating_consistent'], df_grupo1['rating_inconsistent'], df_grupo1['frequency'], color='blue', label='Grupo 1', s=80)
    ax.scatter(df_grupo2['rating_consistent'], df_grupo2['rating_inconsistent'], df_grupo2['frequency'], color='green', label='Grupo 2', s=80)

    for label in grupo1:
        x = df.loc[label, 'rating_consistent']
        y = df.loc[label, 'rating_inconsistent']
        z = df.loc[label, 'frequency']
        ax.text(x, y, z, label, color='blue')

    for label in grupo2:
        x = df.loc[label, 'rating_consistent']
        y = df.loc[label, 'rating_inconsistent']
        z = df.loc[label, 'frequency']
        ax.text(x, y, z, label, color='green')

    ax.set_xlabel('rating_consistent')
    ax.set_ylabel('rating_inconsistent')
    ax.set_zlabel('frequency')
    ax.set_title('Grupos en 3D')
    ax.legend()
    plt.show()
    plt.savefig(ruta_guardado)  # Guardamos la figura
    plt.close()  # Cerramos la figura para no ocupar memoria
    print(f"--> Gráfico guardado en {ruta_guardado}")