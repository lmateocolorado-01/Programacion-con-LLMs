import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

def generar_caso_de_uso_predecir_resistencia():
    # 1. Definir cantidad de datos para entrenar (train) y para predecir (test)
    n_entrenamiento = random.randint(100, 200)
    n_prueba = random.randint(20, 50)
    n_variables = random.randint(4, 8) # Proporciones de la mezcla (cemento, agua, etc.)
    
    # 2. Crear las matrices de datos (X) y los resultados de aprobación (y: 0=Falla, 1=Pasa)
    X_train = np.random.rand(n_entrenamiento, n_variables) * 50
    y_train = np.random.randint(0, 2, size=n_entrenamiento)
    X_test = np.random.rand(n_prueba, n_variables) * 50
    
    # 3. INPUT: Los datos de entrenamiento y los datos nuevos a evaluar
    input_data = {
        'X_train': X_train.copy(),
        'y_train': y_train.copy(),
        'X_test': X_test.copy()
    }
    
    # 4. OUTPUT: Entrenar el modelo "Bosque Aleatorio" y generar las predicciones finales
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    output_esperado = modelo.predict(X_test)
    
    return input_data, output_esperado
