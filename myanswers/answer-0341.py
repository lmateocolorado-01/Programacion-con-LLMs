import pandas as pd
import numpy as np

def preparar_datos(dataset, features, target):
    """
    Prepara los datos para el modelo de predicción de cosecha de gulupa.
    
    Parámetros:
    -----------
    dataset : pd.DataFrame
        DataFrame con los datos históricos de cosecha
    features : list
        Lista de columnas a usar como variables predictoras (X)
        Ej: ['temp_promedio', 'humedad_rel', 'precipitacion_mm', 'edad_cultivo_sem']
    target : str
        Nombre de la columna objetivo (y)
        Ej: 'produccion_kg'
    
    Retorna:
    --------
    X : pd.DataFrame
        Variables predictoras
    y : pd.Series
        Variable objetivo
    """
    X = dataset[features]
    y = dataset[target]
    return X, y
