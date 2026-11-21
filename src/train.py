# Importar librerías
import os
import pandas as pd
import mlflow
import mlflow.sklearn

from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Definir las rutas del proyecto
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Establecer la carpeta principal del proyecto
os.chdir(PROJECT_DIR)

# Configurar MLflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Proyecto_Final_Grado")

# Definir variables predictoras
FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

# Cargar datos de entrenamiento y prueba
train = pd.read_csv(DATA_DIR / "train.csv")
test = pd.read_csv(DATA_DIR / "test.csv")

X_train = train[FEATURES]
y_train = train["species"]

X_test = test[FEATURES]
y_test = test["species"]

# Configurar parámetros del modelo
n_estimators = 100
max_depth = None

# Iniciar experimento en MLflow
with mlflow.start_run(run_name="Random_Forest_Iris"):

    # Registrar parámetros
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("dataset", "Iris")

    # Crear modelo Random Forest
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )

    # Entrenar modelo
    model.fit(X_train, y_train)

    # Realizar predicciones
    predictions = model.predict(X_test)

    # Calcular Accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Registrar métrica
    mlflow.log_metric("accuracy", accuracy)

    # Registrar modelo en MLflow
    mlflow.sklearn.log_model(
        model,
        name="iris_model",
        skops_trusted_types=["sklearn.tree._tree.Tree"]
    )

    # Mostrar resultados
    print("Entrenamiento finalizado correctamente")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Run ID: {mlflow.active_run().info.run_id}")