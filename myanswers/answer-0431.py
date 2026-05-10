import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier


def clasificar_falla_electrica(X_train, y_train, X_test, n_components):
    """
    Clasifica fallas en redes eléctricas usando RobustScaler, PCA y GradientBoostingClassifier.

    Parámetros:
    X_train: datos de entrenamiento
    y_train: etiquetas de entrenamiento
    X_test: datos de prueba
    n_components: número de componentes para PCA

    Retorna:
    numpy array de shape (n_test,) con clases enteras en {0, 1, 2, 3}
    """

    pipeline = Pipeline([
        ('scaler', RobustScaler()),
        ('pca', PCA(n_components=n_components, random_state=42)),
        ('classifier', GradientBoostingClassifier(
            n_estimators=100,
            max_depth=3,
            random_state=42
        ))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    return np.asarray(y_pred, dtype=int)
