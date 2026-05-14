import pandas as pd
import numpy as np

def preparar_datos(dataset, features, target):
    X = dataset[features]
    y = dataset[target]
    return X, y
