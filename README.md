[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11122290&assignment_repo_type=AssignmentRepo)
# Cropped Text Recognition
El objetivo principal de este proyecto es desarrollar e implementar un sistema de reconocimiento de texto capaz de identificar y transcribir el texto presente en imágenes que contengan palabras. 

## Bases de Datos
En este proyecto se utilizaron dos conjuntos de datos diferentes para entrenar y evaluar el sistema de reconocimiento de texto:

### Dataset MJSynth:
MJSynth consiste en datos sintéticos generados automáticamente y contiene alrededor de 90,000 imágenes de palabras en inglés. Estas imágenes de palabras sintéticas fueron creadas mediante la superposición de caracteres en diferentes fondos y variaciones de fuentes. El dataset está disponible en el siguiente enlace: MJSynth Dataset (https://www.robots.ox.ac.uk/~vgg/data/text/)

### IIIT-5K Word Dataset:
Además del dataset sintético MJSynth, se utilizó el dataset IIIT-5K Word para realizar pruebas y evaluaciones. El IIIT-5K Word Dataset consta de aproximadamente 5,000 imágenes de palabras en inglés reales y no sintéticas. Este conjunto de datos fue recolectado y anotado por el Centro de Visión e Imágenes por Computadora (CVIT) del Instituto Internacional de Tecnología de la Información de Hyderabad (IIIT-H). Puedes acceder a este dataset en el siguiente [enlace](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset)

## Estructura de NN
### 1. Redes neuronales convolucionales (CNN)


### 2. Redes neuronales recurrentes (RNN)


### 3. CTC

## Detalles de implementación

## Pruebas / Resultados

## Créditos 

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



## Contributors
Nina Stekacheva Sancho - nina.stekacheva@autonoma.cat
Paula Serrano Sierra - paula.serranos@autonoma.cat

Xarxes Neuronals i Aprenentatge Profund
Grau de Data Engineering, 
UAB, 2023
