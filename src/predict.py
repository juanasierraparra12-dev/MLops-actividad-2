# Importar librerías
import json
import pandas as pd
import mlflow.sklearn

from pathlib import Path

# Definir rutas
PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTRACT_PATH = PROJECT_DIR / "data_contract.json"
MODEL_PATH = PROJECT_DIR / "mlruns"

# Cargar contrato de datos
with open(CONTRACT_PATH, "r", encoding="utf-8") as file:
    contract = json.load(file)

# Configurar MLflow
mlflow.set_tracking_uri(
    f"sqlite:///{(PROJECT_DIR / 'mlflow.db').as_posix()}"
)

# Definir las variables predictoras
FEATURES = list(contract["features"].keys())


# Validar los datos de entrada
def validate_input(data):

    for feature in FEATURES:

        value = data[feature]
        rules = contract["features"][feature]

        if not isinstance(value, (int, float)):
            raise ValueError(f"{feature} debe ser numérico.")

        if not rules["min"] <= value <= rules["max"]:
            raise ValueError(
                f"{feature} está fuera del rango permitido: "
                f"{rules['min']} - {rules['max']}"
            )


# Cargar modelo desde MLflow
def load_model():

    runs = mlflow.search_runs(
        experiment_names=["Proyecto_Final_Grado"],
        order_by=["start_time DESC"]
    )

    if runs.empty:
        raise RuntimeError("No se encontraron modelos registrados.")

    run_id = runs.iloc[0]["run_id"]

    model = mlflow.sklearn.load_model(
        f"runs:/{run_id}/iris_model"
    )

    return model


# Solicitar datos al usuario
def main():

    print("\n===== PREDICCIÓN DE ESPECIES IRIS =====")

    data = {}

    try:
        for feature in FEATURES:
            data[feature] = float(
                input(f"Ingrese {feature}: ")
            )

        # Validar datos
        validate_input(data)

        # Cargar modelo
        model = load_model()

        # Preparar entrada
        input_data = pd.DataFrame([data])

        # Realizar predicción
        prediction = model.predict(input_data)[0]

        # Convertir número en nombre de especie
        species = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        print("\n¡Predicción realizada correctamente!")
        print(f"Especie identificada: {species[prediction]}")

    except ValueError as error:
        print(f"\nERROR DE VALIDACIÓN: {error}")

    except Exception as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()