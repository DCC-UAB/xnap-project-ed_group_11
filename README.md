# Cropped Text Recognition
El objetivo principal de este proyecto es desarrollar e implementar un sistema de reconocimiento de texto capaz de identificar y transcribir el texto presente en imágenes que contengan palabras. 

## 1. Cargar Datos / Bases de Datos

En el proceso de carga de datos, se utilizan los módulos necesarios para obtener las imágenes y sus respectivas etiquetas contenidas en las bases de datos utilizadas. En este proyecto se han utilizado dos conjuntos de datos diferentes para entrenar y evaluar el sistema de reconocimiento de texto:
### 1.1 IIIT-5K Word Dataset

Se ha utilizado para realizar pruebas y evaluaciones. IIIT-5K Word Dataset consta de aproximadamente 5,000 imágenes de palabras en inglés reales y no sintéticas. Este conjunto de datos fue recolectado y anotado por el Centro de Visión e Imágenes por Computadora (CVIT) del Instituto Internacional de Tecnología de la Información de Hyderabad (IIIT-H). 
Para el conjunto de datos IIIT-5K Words, se recopila la imagen y el texto de fuentes separadas. Las palabras se obtienen de un archivo de texto que relaciona los nombres de archivo con las palabras correspondientes.
Propiedad interesate: todas las palabras están en mayúsucula.
### 1.2 Dataset MJSynth

Utilizado para las pruebas oficiales de evaluación. MJSynth consiste en datos sintéticos generados automáticamente y contiene alrededor de 90,000 imágenes de palabras en inglés. 
En el caso de MJSynth, la palabra se extrae directamente del nombre del archivo.
Recalcar que hemos entrenado tan solo con 15G.
## 2. Estructurar NN
### 2.1 Redes neuronales convolucionales (CNN)

La primera etapa consiste en extraer características de la imagen utilizando cinco capas de CNN. Se definen filtros, valores de características, stride y pooling para controlar la reducción de la resolución espacial en cada capa. En cada capa, se realiza una convolución, se aplica normalización, una función de activación ReLU y un max pooling.
### 2.2 Redes neuronales recurrentes (RNN)

A continuación, las características obtenidas en la CNN se pasan a dos capas de RNN, específicamente LSTM (Long-Short Term Memory), que modelan la secuencialidad y las dependencias temporales en el texto. Esto proporciona las probabilidades de clasificación para cada característica, es decir, las probabilidades de que pertenezcan a cada carácter.
### 2.3 Connectionist Temporal Classification CTC

Para alinear la secuencia de entrada con la secuencia de salida, dado que el output es una secuencia de longitud variable, se utiliza el decodificador CTC. Se utiliza un nuevo carácter llamado 'blankspace' para capturar y representar correctamente la estructura y el orden de los elementos en la secuencia de salida, modelando adecuadamente la repetición de caracteres. El repositorio proporciona dos algoritmos de búsqueda para calcular la secuencia más probable: BestPath y BeamSearch.
#### 2.3.1 BestPath

BestPath selecciona el símbolo con mayor probabilidad en cada paso de tiempo y los concatena para formar la secuencia resultante.
#### 2.3.2 BeamSearch

BeamSearch busca las N secuencias más probables (determinado por el tamaño del beam) y selecciona la secuencia final con mayor probabilidad.
#### 2.3.3 Función de pérdida y optimizador

La función de pérdida utilizada es CTC loss, que se calcula como el negativo del logaritmo de la suma de las probabilidades de alineación. Como optimizador, se utiliza Adam (Adaptive Moment Estimation) para una actualización más precisa de los pesos de la red.
### 3. Detalles de implementación

Estructura de Github
```
├── main.py
├── test.py
├── train.py
├── preprocess.py
├── data_loader.py
├── model.py
└── data/
    ├── IIIT/
    └── MJSynth/
```

Se redimensionaron todas las imágenes a un tamaño uniforme de 32x32 píxeles y se normalizaron los valores de los píxeles para asegurar una entrada consistente a la red. Además, se recortaron las regiones de interés que contenían las palabras en cada imagen para reducir el ruido y mejorar la precisión del reconocimiento.

    Configuración de la arquitectura de la red: La red neuronal se compone de cinco capas convolucionales (CNN) seguidas de dos capas recurrentes (RNN) basadas en la arquitectura LSTM. Se utilizaron filtros de diferentes tamaños y se aplicó la función de activación ReLU después de cada capa convolucional para introducir la no linealidad en la red. Las capas recurrentes LSTM permitieron modelar la secuencialidad y las dependencias temporales en el texto.

    Entrenamiento del modelo: El modelo se entrenó utilizando el algoritmo de optimización Adam con una tasa de aprendizaje inicial de 0.001. Se utilizó un tamaño de lote de 32 y se realizaron 20 épocas de entrenamiento. Durante el entrenamiento, se aplicó la técnica de regularización de dropout con una tasa de 0.5 para evitar el sobreajuste.

    Evaluación y métricas: Para evaluar el rendimiento del modelo, se utilizó la precisión y la pérdida como métricas principales. La precisión se calculó como la proporción de palabras correctamente reconocidas en el conjunto de prueba. La pérdida se calculó utilizando la función de pérdida CTC para medir la diferencia entre las etiquetas predichas y las reales.
    
### 4. Pruebas / Resultados
Se han tenido en cuenta dos casos. El entrenamiento teniendo en cuenta cada uno de los carácteres posibles (mayúsculas y minúsuculas incluidas) y solo minúsculas, ya que son los valores que mas predominan en nuestro dataset.
A continuación se presentan los valores de precisión y pérdida obtenidos en la prueba con ambos algoritmos de búsqueda. Teniendo en cuenta todos los chars posibles (mayúsculas y minúsculas).

#### 4.1 Utilizando Mayúsuculas y Minúsculas

#### BestPath - MJSynth
<img src="doc/bestpath_allchars_loss.png" alt="BestPath - MJSynth - loss" width="500">
La función de pérdida alcanza un valor de 6.2, lo cual indica que el modelo tiene un nivel moderado de error en la tarea de reconocimiento de texto. Esto sugiere que el modelo necesita ajustes adicionales para mejorar su rendimiento.
<img src="doc/bestpath_allchars_accuracy.png" alt="BestPath - MJSynth - accuracy" width="500">
La precisión alcanza un valor del 64.8%, lo que significa que el modelo acierta correctamente aproximadamente el 64.8% de las muestras evaluadas. Si bien esta precisión es aceptable, aún hay margen para mejorar el rendimiento del modelo y aumentar la precisión en futuras iteraciones.
<img src="doc/bestpath_allchars_cm.png" alt="BestPath - MJSynth - cm" width="500">
La matriz de confusión muestra una línea diagonal pronunciada, lo cual indica que la mayoría de las predicciones son correctas. Sin embargo, se observa una línea paralela a la diagonal, lo que sugiere que el modelo tiende a confundir mayúsculas y minúsculas en algunas letras. Específicamente, se observa que las letras "e" y "i" son más propensas a ser confundidas. Además, se aprecia que el modelo tiende a predecir más letras en minúsculas que en mayúsculas.

#### BestPath - IIIT
<img src="doc/bestpath_allchars_iiit.png" alt="BestPath - IIIT" width="500">
Se ha obtenido una precisión del 80.3%, lo que indica que el modelo tiene un alto rendimiento en la tarea de reconocimiento de texto. Esta precisión es considerablemente mayor que en el caso anterior, lo cual sugiere que el modelo está funcionando mejor en un conjunto de datos en el que solo hay letras mayúsculas.

La función de pérdida es de 2.1, lo que indica que el modelo tiene un nivel bajo de error. Este resultado es coherente con la alta precisión obtenida, lo que sugiere que el modelo ha aprendido eficazmente las características.

En este conjunto de datos, solo se encuentran letras mayúsculas. Este hecho nos puede indicar que uno de los cuellos de botella se encuentra en el aprendizaje de las variaciones entre letras mayúsculas y minúsculas.

#### BeamSearch - MJSynth
<img src="doc/beamsearch_allchars_loss.png" alt="BeamSearch - MJSynth - loss" width="500">
<img src="doc/beamsearch_allchars_accuracy.png" alt="BeamSearch - MJSynth - accuracy" width="500">
<img src="doc/beamsearch_allchars_cm.png" alt="BeamSearch - MJSynth - cm" width="500">
Es interesante observar que, a pesar de cambiar el algoritmo de decodificación, los resultados obtenidos siguen siendo similares, con una precisión de alrededor de 63.5% y una pérdida de alrededor de 5.8%. Esto sugiere que la restricción en el rendimiento del sistema no se encuentra en el algoritmo de decodificación en sí.

#### 4.2 Uso exclusivo de minúsculas
Después de realizar un análisis exhaustivo, descubrimos que el número de minúsculas en el dataset es significativamente mayor, con 9,193,336 minúsculas en comparación con 5,264,306 mayúsculas. 

#### BestPath - MJSynth
<img src="doc/beamsearch_allchars_loss.png" alt="BeamSearch - MJSynth - loss" width="500">
<img src="doc/beamsearch_allchars_accuracy.png" alt="BeamSearch - MJSynth - accuracy" width="500">
<img src="doc/beamsearch_allchars_cm.png" alt="BeamSearch - MJSynth - cm" width="500">

#### BeamSearch - MJSynth
<img src="doc/beamsearch_allchars_loss.png" alt="BeamSearch - MJSynth - loss" width="500">
<img src="doc/beamsearch_allchars_accuracy.png" alt="BeamSearch - MJSynth - accuracy" width="500">
<img src="doc/beamsearch_allchars_cm.png" alt="BeamSearch - MJSynth - cm" width="500">


### 5. Créditos

A continuación, se mencionan los créditos y las fuentes utilizadas en el desarrollo del proyecto:

 - IIIT-5K Word Dataset: El conjunto de datos fue recolectado y anotado por el Centro de Visión e Imágenes por Computadora (CVIT) del Instituto Internacional de Tecnología de la Información de Hyderabad (IIIT-H). Puedes acceder a este dataset en el siguiente [enlace](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset).

 - MJSynth Dataset: Este dataset fue generado automáticamente y está disponible en el siguiente [enlace](https://www.robots.ox.ac.uk/~vgg/data/text/).

 - Código base del proyecto: El código base utilizado en este proyecto se basa en el repositorio SimpleHTR desarrollado por [Harald Scheidl](https://github.com/githubharald).

## Colaboradores
Nina Stekacheva Sancho - nina.stekacheva@autonoma.cat
Paula Serrano Sierra - paula.serranos@autonoma.cat

Xarxes Neuronals i Aprenentatge Profund
Grau de Data Engineering, 
UAB, 2023
