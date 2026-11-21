# Importar librerías
import pandas as pd
from pathlib import Path

# Definir la ruta de los datos
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Definir las variables predictoras
FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

# Definir la variable objetivo
TARGET = "species"

# Definir rangos permitidos para las variables
RANGES = {
    "sepal length (cm)": (4.0, 8.0),
    "sepal width (cm)": (2.0, 5.0),
    "petal length (cm)": (1.0, 7.0),
    "petal width (cm)": (0.1, 3.0)
}


def validate_data(file_path):

    # Cargar archivo CSV
    df = pd.read_csv(file_path)

    # Verificar columnas requeridas
    required_columns = FEATURES + [TARGET]

    if list(df.columns) != required_columns:
        raise ValueError("Las columnas del dataset no son correctas.")

    # Verificar valores nulos
    if df.isnull().values.any():
        raise ValueError("Se encontraron valores nulos.")

    # Verificar tipos de datos
    for column in required_columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"La columna {column} debe ser numérica.")

    # Verificar rangos de las variables
    for column, (minimum, maximum) in RANGES.items():
        if not df[column].between(minimum, maximum).all():
            raise ValueError(
                f"La columna {column} tiene valores fuera del rango permitido."
            )

    # Verificar clases permitidas
    if not df[TARGET].isin([0, 1, 2]).all():
        raise ValueError("La variable species contiene clases no permitidas.")

    print(f"Validación correcta: {file_path.name}")

    return True


# Ejecutar validación de los archivos
if __name__ == "__main__":

    validate_data(DATA_DIR / "train.csv")
    validate_data(DATA_DIR / "test.csv")

    print("Todos los datos cumplen el contrato.")