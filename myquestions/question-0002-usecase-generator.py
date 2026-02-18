El Problema:
Tienes una matriz de datos con los resultados de múltiples ensayos de laboratorio sobre muestras de suelo (humedad, densidad, cohesión, etc.). Necesitas clasificar estos suelos en diferentes zonas con características similares para definir la estrategia de cimentación, pero no tienes etiquetas previas.

Tu Misión:
Escribe una función llamada agrupar_tipos_suelo(X, num_grupos) que realice lo siguiente:
Reciba una matriz de características X (array de numpy o DataFrame) y un entero num_grupos.
Instancie y entrene un modelo KMeans de sklearn.cluster usando el número de grupos especificado y un random_state=42 para reproducibilidad.
Devuelva un array de numpy con las etiquetas de los clústeres asignados a cada muestra de suelo.
