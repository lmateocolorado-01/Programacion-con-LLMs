import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_filtrar_presupuestos():
    n_rows = random.randint(10, 20)
    
    data = {
        'id_proyecto': [f'PRJ-{i:03d}' for i in range(n_rows)],
        'presupuesto_inicial': np.random.uniform(10000, 50000, n_rows),
        'costo_ejecutado': np.random.uniform(8000, 60000, n_rows)
    }
    df = pd.DataFrame(data)
    
    mask = np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
    df.loc[mask, 'costo_ejecutado'] = np.nan
    
    input_data = {'df': df.copy()}
    
    df_expected = df.copy()
    df_expected = df_expected.dropna(subset=['costo_ejecutado'])
    df_expected['desviacion_costo'] = df_expected['costo_ejecutado'] - df_expected['presupuesto_inicial']
    df_expected = df_expected[df_expected['desviacion_costo'] > 0]
    df_expected = df_expected.sort_values(by='desviacion_costo', ascending=False)
    
    output_data = df_expected
    
    return input_data, output_data
