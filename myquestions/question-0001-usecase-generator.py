import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_filtrar_presupuestos():
    # 1. Definir una cantidad aleatoria de proyectos (entre 10 y 20)
    n_rows = random.randint(10, 20)
    
    # 2. Crear datos ficticios con numpy
    data = {
        'id_proyecto': [f'PRJ-{i:03d}' for i in range(n_rows)],
        'presupuesto_inicial': np.random.uniform(10000, 50000, n_rows),
        'costo_ejecutado': np.random.uniform(8000, 60000, n_rows)
    }
    df = pd.DataFrame(data)
    
    # 3. Simular un 20% de celdas vacías (NaN) en la columna de costo ejecutado
    mask = np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
    df.loc[mask, 'costo_ejecutado'] = np.nan
    
    # 4. INPUT: Lo que recibe el estudiante (usamos .copy() para no dañar los datos originales)
    input_data = {'df': df.copy()}
    
    # 5. OUTPUT: La solución paso a paso que debe lograr el estudiante
    df_expected = df.copy()
    df_expected = df_expected.dropna(subset=['costo_ejecutado']) # a. Borrar nulos
    df_expected['desviacion_costo'] = df_expected['costo_ejecutado'] - df_expected['presupuesto_inicial'] # b. Calcular diferencia
    df_expected = df_expected[df_expected['desviacion_costo'] > 0] # c. Filtrar sobrecostos
    df_expected = df_expected.sort_values(by='desviacion_costo', ascending=False) # d. Ordenar
    
    output_data = df_expected
    
    return input_data, output_data



entrada, salida = generar_caso_de_uso_filtrar_presupuestos()
print("--- INPUT --- \n", entrada)
print("\n--- OUTPUT ESPERADO --- \n", salida)
