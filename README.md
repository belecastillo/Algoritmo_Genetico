## Algoritmo Genético

Este proyecto aborda el problema del particionamiento de datos en dos grupos homogéneos de manera a que cada individuo del grupo 1 tenga su correspondiente en el grupo 2. La implementación esta basado en el concepto de Algortimos Géneticos, una técnica de optimización inspirada en la evolución biológica. En este trabajo, para medir la homogeneidad de la partición, utilizamos la suma de los cuadrados de las distancias entre cada par de elementos emparejados en los subconjuntos.

## Instalación

1. Clonar el repositorio:
```bash
   git clone https://github.com/belecastillo/Algoritmo_Genetico.git
 ```
2. Ir a la carpeta del Proyecto:
```bash
   cd algoritmo_genetico
```
3. Crear y activar entorno virtual:
- En Windows:
```bash
   python -m venv venv
   venv\Scripts\activate
 ```
- En Linux:
```bash
   python3 -m venv venv
   source venv/bin/activate
 ```
4. Instalar dependecias:
```bash
   pip install -r requirements.txt
 ```


## Ejecución

1. Ejecutar con:
```bash
    python -m src.main
```