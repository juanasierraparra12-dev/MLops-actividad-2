## Manual de instalación, configuración y ejecución

### 1. Descripción del proyecto

Este proyecto implementa un pipeline automatizado de Machine Learning utilizando el conjunto de datos Iris el cual cuenta con cierta informacion de unas especies de flores, en se utilizo un algoritmo llamado Random Forest Classifier.

Este sistema integra las difernetes etapas de preparación de datos, validación de calidad, entrenamiento del modelo, registro de experimentos mediante MLflow y ejecución de pruebas automatizadas.

Adicionalmente, incorpora un mecanismo de inferencia que permite ingresar las características de una flor desde la terminal y tambien permite que se ingrese un tipo de flor y que verifique si esta en los datos o no, etso lo gace mediante la validacion de los datos mediante un contrato JSON y obtener la especie predicha por el modelo.

El objetivo es garantizar la reproducibilidad del proceso y facilitar su ejecución mediante un único comando.

### 2. Requisitos previos

Para ejecutar correctamente el proyecto se requiere:

- Sistema operativo Windows.
- Python 3.13.
- Visual Studio Code.
- Git.
- PowerShell.
- Conexión a Internet para descargar las dependencias.

### 3. Descarga del proyecto

Primero, se debera copiar el repositorio de GitHub.

Abrir PowerShell y ejecutar:

```powershell
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta descargada:

```powershell
cd "Actividad 2"
```

Abrir el proyecto en Visual Studio Code:

### 4. Configuración del entorno virtual

Para mantener aisladas las dependencias del proyecto, se debe crear un entorno virtual.

**4.1. Crear el entorno virtual**

```powershell
py -3.13 -m venv .venv
```

**4.2. Activar el entorno virtual**

```powershell
.venv\Scripts\activate
```

Si PowerShell bloquea la ejecución de scripts, ejecutar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Posteriormente, activar nuevamente el entorno:

```powershell
.venv\Scripts\activate
```

**4.3. Instalar las dependencias**

Con el entorno virtual activo, ejecutar:

```powershell
python -m pip install -r requirements.txt
```

Las dependencias instaladas son:

- mlflow
- scikit-learn
- pandas
- pytest

### 5. Estructura del proyecto

El proyecto presenta la siguiente organización:



 data/
   train.csv
   test.csv

 mlruns/

 src/
   prepare.py
   validate_data.py
   train.py
   predict.py
   validate_date.py

 tests/
   test_model.py

 data_contract.json
  mlflow.db
 requirements.txt
 run_pipeline.py
 README.md


**Descripción de los archivos:**

- `prepare.py`: carga el dataset Iris, realiza la división estratificada 80/20 y genera los archivos de entrenamiento y prueba.
- `validate_data.py`: verifica los tipos de datos, la ausencia de valores nulos y los rangos permitidos.
- `train.py`: entrena el modelo Random Forest y registra los parámetros, métricas y modelo en MLflow.
- `predict.py`: permite ingresar datos desde la terminal, validar las características y obtener predicciones.
- `test_model.py`: ejecuta pruebas automatizadas sobre los archivos y el modelo.
- `data_contract.json`: establece las reglas que deben cumplir los datos de entrada, incluyendo ejemplos válidos e inválidos.
- `run_pipeline.py`: coordina la ejecución automática de las diferentes etapas.
- `requirements.txt`: contiene las dependencias necesarias.
- `mlflow.db`: almacena información de los experimentos.
- `mlruns/`: contiene archivos asociados al seguimiento de los experimentos y modelos.

Las carpetas `data`, `mlruns` y los archivos de seguimiento de MLflow pueden generarse durante la ejecución del proyecto.

### 6. Ejecución del pipeline automatizado

Una vez configurado el entorno e instaladas las dependencias, ubicarse en la carpeta principal del proyecto.

Ejecutar el siguiente comando:

```powershell
python run_pipeline.py
```

El archivo ejecuta automáticamente cuatro etapas:

**ETAPA 1. Preparación de datos**

Carga Iris desde Scikit-learn y genera:

- train.csv: 120 registros.
- test.csv: 30 registros.

La división se realiza utilizando una proporción 80/20 y estratificación.

**ETAPA 2. Validación y control de calidad**

Comprueba que los datos cumplan las condiciones establecidas:

- Tipos de datos numéricos.
- Ausencia de valores nulos.
- Rangos permitidos.
- Clases válidas de la variable objetivo.

**ETAPA 3. Entrenamiento y registro con MLflow**

Entrena un modelo Random Forest Classifier con los siguientes parámetros:

- n_estimators: 100.
- max_depth: None.
- random_state: 42.

Calcula la métrica Accuracy y registra los resultados en MLflow.

**ETAPA 4. Pruebas automatizadas**

Ejecuta las pruebas definidas en `test_model.py` mediante Pytest.

### 7. Ejecución de predicciones (Inferencia)

El proyecto permite utilizar el modelo entrenado para clasificar nuevas observaciones del conjunto Iris.

Para realizar una predicción, ejecutar:

```powershell
python src/predict.py
```

El programa solicitará las cuatro características de la flor:

- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)

Los datos ingresados serán comparados con las reglas definidas en `data_contract.json`.

Si cumplen las condiciones, el modelo realizará la predicción y mostrará la especie correspondiente.

Las clases utilizadas son:

| Código | Especie |
|---|---|
| 0 | Setosa |
| 1 | Versicolor |
| 2 | Virginica |

Si los valores ingresados están fuera de los rangos permitidos, el sistema rechazará la entrada y mostrará el mensaje de validación correspondiente.

**Ejemplo de entrada válida:**

```text
sepal length: 5.1
sepal width: 3.5
petal length: 1.4
petal width: 0.2
```

Resultado esperado:

Predicción realizada correctamente.
Especie identificada: Setosa

### 8. Comprobación interactiva de especies

El proyecto incorpora una funcionalidad de validación interactiva que permite comprobar si una especie ingresada por el usuario pertenece a las clases disponibles en el conjunto de datos Iris.

Esta funcionalidad se encuentra en el archivo `tests/test_validation.py` y permite verificar el comportamiento del sistema mediante diferentes entradas desde la terminal.

**8.1. Ejecución**

Para realizar la comprobación de manera independiente, ubicarse en la carpeta principal del proyecto y ejecutar:

```powershell
python tests/test_validation.py
```

También se puede ejecutar como parte del proceso automatizado mediante:

```powershell
python run_pipeline.py
```

**8.2. Ingreso de datos**

Al ejecutar el programa, aparecerá la siguiente solicitud:

```text
===== VALIDACIÓN DE ESPECIES IRIS =====

Ingrese el número de especie:
```

El usuario debe ingresar un número entero correspondiente a una de las especies disponibles.

**8.3. Especies permitidas**

El conjunto de datos Iris contiene tres clases:


 0  Setosa 
 1  Versicolor 
 2  Virginica 

**8.4. Validaciones realizadas**

El programa ejecuta tres etapas:

- **Etapa 1. Verificación del tipo de dato:** comprueba que la entrada sea un número entero.
- **Etapa 2. Verificación de especies:** comprueba que el número ingresado pertenezca a las clases disponibles (0, 1 o 2).
- **Etapa 3. Identificación de la especie:** muestra el nombre correspondiente cuando las validaciones anteriores son satisfactorias.

Si alguna validación falla, el proceso se detiene y muestra el error correspondiente.

**8.5. Ejemplos de ejecución**

**Ejemplo 1. Entrada válida**

Entrada:


Ingrese el número de especie: 1


Resultado esperado:

ETAPA 1: VERIFICACIÓN DEL TIPO DE DATO
Resultado: APROBADO

ETAPA 2: VERIFICACIÓN DE ESPECIES
Resultado: APROBADO

ETAPA 3: IDENTIFICACIÓN DE LA ESPECIE
Resultado: APROBADO
Especie identificada: versicolor

VALIDACIÓN FINALIZADA CORRECTAMENTE
```

**Ejemplo 2. Entrada inválida**

Entrada:

Ingrese el número de especie: 5


Resultado esperado:

ETAPA 1: VERIFICACIÓN DEL TIPO DE DATO
Resultado: APROBADO

ETAPA 2: VERIFICACIÓN DE ESPECIES
Resultado: RECHAZADO

Error: La especie 5 no existe.
Valores permitidos: [0, 1, 2]

PIPELINE DETENIDO EN ETAPA 2

**Ejemplo 3. Tipo de dato incorrecto**

Entrada:
Ingrese el número de especie: hola


Resultado esperado:
ETAPA 1: VERIFICACIÓN DEL TIPO DE DATO
Resultado: RECHAZADO

Error: Se debe ingresar un número entero.

PIPELINE DETENIDO EN ETAPA 1

Esta funcionalidad permite demostrar cómo el sistema identifica entradas válidas e inválidas, controla los datos ingresados y detiene el proceso cuando se presenta una condición que no cumple las reglas establecidas.

### 9. Consulta de experimentos en MLflow

Para visualizar los experimentos registrados, abrir una segunda terminal de PowerShell.

Activar el entorno virtual y ejecutar:

```powershell
mlflow ui