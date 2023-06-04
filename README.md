<img src="doc/beamsearch_allchars_loss.png" alt="Descripción de la imagen" width="500">

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

    Preprocesamiento de imágenes: Se redimensionaron todas las imágenes a un tamaño uniforme de 32x32 píxeles y se normalizaron los valores de los píxeles para asegurar una entrada consistente a la red. Además, se recortaron las regiones de interés que contenían las palabras en cada imagen para reducir el ruido y mejorar la precisión del reconocimiento.

    Configuración de la arquitectura de la red: La red neuronal se compone de cinco capas convolucionales (CNN) seguidas de dos capas recurrentes (RNN) basadas en la arquitectura LSTM. Se utilizaron filtros de diferentes tamaños y se aplicó la función de activación ReLU después de cada capa convolucional para introducir la no linealidad en la red. Las capas recurrentes LSTM permitieron modelar la secuencialidad y las dependencias temporales en el texto.

    Entrenamiento del modelo: El modelo se entrenó utilizando el algoritmo de optimización Adam con una tasa de aprendizaje inicial de 0.001. Se utilizó un tamaño de lote de 32 y se realizaron 20 épocas de entrenamiento. Durante el entrenamiento, se aplicó la técnica de regularización de dropout con una tasa de 0.5 para evitar el sobreajuste.

    Evaluación y métricas: Para evaluar el rendimiento del modelo, se utilizó la precisión y la pérdida como métricas principales. La precisión se calculó como la proporción de palabras correctamente reconocidas en el conjunto de prueba. La pérdida se calculó utilizando la función de pérdida CTC para medir la diferencia entre las etiquetas predichas y las reales.
    
### 4. Pruebas / Resultados
Se han tenido en cuenta dos casos. El entrenamiento teniendo en cuenta cada uno de los carácteres posibles (mayúsculas y minúsuculas incluidas) y solo minúsculas, ya que son los valores que mas predominan en nuestro dataset.
A continuación se presentan los valores de precisión y pérdida obtenidos en la prueba con ambos algoritmos de búsqueda. Teniendo en cuenta todos los chars posibles (mayúsculas y minúsculas).

#### 4.1 Utilizando Mayúsuculas y Minúsculas
BestPath - MJSynth
![BestPath - MJSynth - loss](doc/bestpath_allchars_loss.png)
![BestPath - MJSynth - accuracy](doc/bestpath_allchars_accuracy.png)
![BestPath - MJSynth - cm](doc/bestpath_allchars_cm.png)

BestPath - IIIT
![BestPath - IIT](doc/bestpath_allchars_iiit.png)

BeamSearch - MJSynth
![BeamSearch - MJSynth - loss](doc/beamsearch_allchars_loss.png)
![BeamSearch - MJSynth - accuracy](doc/beamsearch_allchars_accuracy.png)
![BeamSearch - MJSynth - cm](doc/beamsearch_allchars_cm.png)

<img src="doc/beamsearch_allchars_loss.png" alt="Descripción de la imagen" width="1000">




#### 4.2 Uso exclusivo de minúsculas
BestPath
![BestPath - MJSynth](https://github.com/DCC-UAB/xnap-project-ed_group_11/blob/main/doc/beamsearch_allchars_loss.png)
BeamSearch
![BestPath - MJSynth](https://github.com/DCC-UAB/xnap-project-ed_group_11/blob/main/doc/beamsearch_allchars_loss.png)

Se presentan los valores de precisión y pérdida obtenidos en la prueba con ambos algoritmos de búsqueda. No se observaron mejoras significativas, lo que indica que el cuello de botella se encuentra en el reconocimiento de caracteres y no en la decodificación.
### 5. Créditos

A continuación, se mencionan los créditos y las fuentes utilizadas en el desarrollo del proyecto:

 - IIIT-5K Word Dataset: El conjunto de datos fue recolectado y anotado por el Centro de Visión e Imágenes por Computadora (CVIT) del Instituto Internacional de Tecnología de la Información de Hyderabad (IIIT-H). Puedes acceder a este dataset en el siguiente [enlace](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset).

 - MJSynth Dataset: Este dataset fue generado automáticamente y está disponible en el siguiente [enlace](https://www.robots.ox.ac.uk/~vgg/data/text/).

 - Código base del proyecto: El código base utilizado en este proyecto se basa en el repositorio SimpleHTR desarrollado por [Harald Scheidl](https://github.com/githubharald).


Recuerda citar adecuadamente estas fuentes si utilizas este proyecto como referencia o base para tu propia implementación.

## Code structure
You must create as many folders as you consider. You can use the proposed structure or replace it by the one in the base code that you use as starting point. Do not forget to add Markdown files as needed to explain well the code and how to use it.

## Example Code
The given code is a simple CNN example training on the MNIST dataset. It shows how to set up the [Weights & Biases](https://wandb.ai/site)  package to monitor how your network is learning, or not.

Before running the code you have to create a local environment with conda and activate it. The provided [environment.yml](https://github.com/DCC-UAB/XNAP-Project/environment.yml) file has all the required dependencies. Run the following command: ``conda env create --file environment.yml `` to create a conda environment with all the required dependencies and then activate it:
```
conda activate xnap-example
```

To run the example code:
```
python main.py
```



## Colaboradores
Nina Stekacheva Sancho - nina.stekacheva@autonoma.cat
Paula Serrano Sierra - paula.serranos@autonoma.cat

Xarxes Neuronals i Aprenentatge Profund
Grau de Data Engineering, 
UAB, 2023
