# Importar librerías
import subprocess
import sys
from pathlib import Path

# Definir ruta principal del proyecto
PROJECT_DIR = Path(__file__).resolve().parent


def ejecutar_etapa(nombre, comando):

    print(f"\n{'=' * 50}")
    print(nombre)
    print("=" * 50)

    subprocess.run(
        comando,
        cwd=PROJECT_DIR,
        check=True
    )


def main():

    print("\nINICIANDO PIPELINE DE MACHINE LEARNING CON IRIS")

    # ETAPA 1: Preparación de datos
    ejecutar_etapa(
        "ETAPA 1: Preparación de datos",
        [sys.executable, "src/prepare.py"]
    )

    # ETAPA 2: Validación de datos
    ejecutar_etapa(
        "ETAPA 2: Validación y control de calidad",
        [sys.executable, "src/validate_data.py"]
    )

    # ETAPA 3: Entrenamiento y registro en MLflow
    ejecutar_etapa(
        "ETAPA 3: Entrenamiento y registro con MLflow",
        [sys.executable, "src/train.py"]
    )

    # ETAPA 4: Pruebas automatizadas
    ejecutar_etapa(
        "ETAPA 4: Pruebas automatizadas",
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/test_model.py",
            "-v"
        ]
    )

    print("\nPIPELINE FINALIZADO CORRECTAMENTE")

    # ETAPA 5: Demostración interactiva
    ejecutar_etapa(
        "ETAPA 5: Demostración interactiva de validación",
        [sys.executable, "tests/test_validation.py"]
    )


if __name__ == "__main__":
    main()