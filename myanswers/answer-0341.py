import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def preparar_datos(dataset, features, target):
    X = dataset[features]
    y = dataset[target]

    return X, y


def predecir_cosecha_gulupa(dataset, condiciones_actuales):
    features = [
        "temp_promedio",
        "humedad_rel",
        "precipitacion_mm",
        "edad_cultivo_sem"
    ]

    target = "produccion_kg"

    X = dataset[features]
    y = dataset[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    condiciones_actuales = np.array(condiciones_actuales).reshape(1, -1)

    prediccion = modelo.predict(condiciones_actuales)

    return float(prediccion[0])
