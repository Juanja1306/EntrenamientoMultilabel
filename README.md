# Análisis, Entrenamiento y Predicción de Imágenes

## Descripción General
Este proyecto aborda el ciclo completo de análisis, entrenamiento y predicción utilizando un conjunto de imágenes. Cada parte del proyecto se desarrolla en un cuaderno Jupyter, que permite seguir paso a paso el proceso desde la exploración inicial de datos hasta la aplicación práctica de un modelo de aprendizaje automático para realizar predicciones.

## Cuadernos

### 1. Análisis Exploratorio (`1_AnalisisExploratorio.ipynb`)
- **Objetivo**: Analizar y preparar el conjunto de imágenes para el entrenamiento del modelo.
- **Contenido**:
  - Importación de bibliotecas y datos.
  - Conteo y verificación de la distribución de las imágenes por categoría.
  - Creación de un dataset coherente para el entrenamiento.
  - Normalización de imágenes para asegurar la uniformidad en el input del modelo.
  - Verificación de la correcta etiquetación de las imágenes.

### 2. Entrenamiento (`2_Entrenamiento.ipynb`)
- **Objetivo**: Entrenar un modelo de red neuronal para la clasificación de imágenes.
- **Contenido**:
  - Configuración de CUDA para aprovechar capacidades de procesamiento en GPU.
  - Carga de la arquitectura de la red neuronal adecuada para el tipo de datos.
  - Definición del número de categorías de salida basado en el análisis exploratorio.
  - Proceso de entrenamiento detallado, incluyendo la evaluación de la calidad del modelo.
  - Almacenamiento de los pesos del modelo para su uso futuro.

### 3. Carga y Predicción (`3_Carga_Prediccion.ipynb`)
- **Objetivo**: Utilizar el modelo entrenado para hacer predicciones sobre nuevas imágenes.
- **Contenido**:
  - Carga del modelo con los pesos previamente guardados.
  - Importación y preparación de nuevas imágenes para testear el modelo.
  - Realización de predicciones y visualización de los resultados.

## Instalación y Configuración
Asegúrate de tener Python y Jupyter instalados en tu sistema. Luego, instala las dependencias necesarias con el siguiente comando:

```bash
pip install numpy pandas matplotlib torch torchvision
