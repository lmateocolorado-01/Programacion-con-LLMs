import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_resumir_interferencias():
    # 1. Generar entre 50 y 150 reportes de colisiones (clashes)
    n_rows = random.randint(50, 150)
    niveles = ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4', 'Cubierta']
    
    # 2. Asignar un ID único y un nivel aleatorio a cada interferencia
    data = {
        'id_clash': [f'CL-{random.randint(1000, 9999)}' for _ in range(n_rows)],
        'nivel_edificio': np.random.choice(niveles, n_rows)
    }
    df = pd.DataFrame(data)
    
    # 3. INPUT: El DataFrame crudo que debe procesar el estudiante
    input_data = {'df': df.copy()}
    
    # 4. OUTPUT: Agrupar por nivel y contar cuántos clashes hay en cada uno
    df_expected = df.groupby('nivel_edificio')[['id_clash']].count()
    df_expected = df_expected.rename(columns={'id_clash': 'total_conflictos'}) # Renombrar la columna
    
    output_data = df_expected
    
    return input_data, output_data
