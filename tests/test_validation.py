# Importar librerías
from sklearn.datasets import load_iris

# Cargar dataset Iris
iris = load_iris()

# Obtener especies permitidas
ESPECIES_VALIDAS = list(range(len(iris.target_names)))


def validar_especie():

    print("\n===== VALIDACIÓN DE ESPECIES IRIS =====")

    # Solicitar dato al usuario
    valor = input("\nIngrese el número de especie: ")

    # ETAPA 1: Validación del tipo de dato
    print("\nETAPA 1: VERIFICACIÓN DEL TIPO DE DATO")

    try:
        especie = int(valor)
        print("Resultado: APROBADO")

    except ValueError:
        print("Resultado: RECHAZADO")
        print("Error: Se debe ingresar un número entero.")
        print("\nPIPELINE DETENIDO EN ETAPA 1")
        return

    # ETAPA 2: Validación de especies permitidas
    print("\nETAPA 2: VERIFICACIÓN DE ESPECIES")

    if especie not in ESPECIES_VALIDAS:

        print("Resultado: RECHAZADO")
        print(f"Error: La especie {especie} no existe.")
        print(f"Valores permitidos: {ESPECIES_VALIDAS}")
        print("\nPIPELINE DETENIDO EN ETAPA 2")
        return

    print("Resultado: APROBADO")

    # ETAPA 3: Identificación de la especie
    print("\nETAPA 3: IDENTIFICACIÓN DE LA ESPECIE")

    nombre = iris.target_names[especie]

    print("Resultado: APROBADO")
    print(f"Especie identificada: {nombre}")

    print("\nVALIDACIÓN FINALIZADA CORRECTAMENTE")


if __name__ == "__main__":
    validar_especie()