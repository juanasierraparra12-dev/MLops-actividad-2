# Importar librerías
import pandas as pd
import mlflow.sklearn

from pathlib import Path
from sklearn.metrics import accuracy_score

# Definir rutas
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_DIR = PROJECT_DIR / "mlruns"

# Prueba 1: verificar que existan los archivos
def test_files_exist():
    assert (DATA_DIR / "train.csv").exists()
    assert (DATA_DIR / "test.csv").exists()


# Prueba 2: verificar que los archivos tengan registros
def test_data_not_empty():
    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")

    assert len(train) > 0
    assert len(test) > 0


# Prueba 3: verificar que el modelo pueda entrenarse y predecir
def test_model_prediction():
    from sklearn.ensemble import RandomForestClassifier

    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")

    features = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(train[features], train["species"])

    predictions = model.predict(test[features])

    assert len(predictions) == len(test)


# Prueba 4: verificar Accuracy mínima
def test_accuracy_minimum():
    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")

    features = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]

    from sklearn.ensemble import RandomForestClassifier

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(train[features], train["species"])

    predictions = model.predict(test[features])

    accuracy = accuracy_score(test["species"], predictions)

    assert accuracy >= 0.80