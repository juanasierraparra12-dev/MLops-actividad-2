
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from pathlib import Path


iris = load_iris()

# Crear DataFrame con las variables predictoras
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# Crear variable objetivo
y = pd.Series(iris.target, name="species")

# Unir variables predictoras y objetivo
df = X.copy()
df["species"] = y

# Separar datos de entrenamiento y prueba (80/20)
train, test = train_test_split(
    df,
    test_size=0.20,
    random_state=42,
    stratify=df["species"]
)

# Crear carpeta data si no existe
data_dir = Path(__file__).resolve().parent.parent / "data"
data_dir.mkdir(exist_ok=True)

# Guardar archivos CSV
train.to_csv(data_dir / "train.csv", index=False)
test.to_csv(data_dir / "test.csv", index=False)

print("Preparación de datos finalizada correctamente")
print(f"Registros de entrenamiento: {len(train)}")
print(f"Registros de prueba: {len(test)}")