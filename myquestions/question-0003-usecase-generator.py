import numpy as np
from sklearn.cluster import KMeans
import random

def generar_caso_de_uso_agrupar_tipos_suelo():
    # 1. Crear aleatoriamente el número de muestras, variables (ej: humedad, densidad) y grupos
    n_muestras = random.randint(50, 150)
    n_caracteristicas = random.randint(3, 6)
    num_grupos = random.randint(2, 5)
    
    # 2. Generar una matriz de datos (X) con valores entre 0 y 100
    X = np.random.rand(n_muestras, n_caracteristicas) * 100
    
    # 3. INPUT: La matriz de datos y el número de clústeres a formar
    input_data = {
        'X': X.copy(),
        'num_grupos': num_grupos
    }
    
    # 4. OUTPUT: Entrenar el modelo KMeans y predecir a qué grupo pertenece cada suelo
    modelo = KMeans(n_clusters=num_grupos, random_state=42, n_init='auto')
    output_esperado = modelo.fit_predict(X)
    
    return input_data, output_esperado
