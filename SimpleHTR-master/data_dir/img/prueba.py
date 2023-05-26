# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:00:46 2023

@author: paula
"""

import os
import cv2

lista_alto, lista_ancho = [], []

# Ruta del directorio que contiene las imágenes
directorio = '.'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Recorrer cada archivo en el directorio
for archivo in archivos:
    # Ruta completa del archivo
    ruta_archivo = os.path.join(directorio, archivo)
    
    # Verificar si el archivo es una imagen
    if os.path.isfile(ruta_archivo) and archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Leer la imagen utilizando OpenCV
        imagen = cv2.imread(ruta_archivo)
        
        # Obtener el tamaño de la imagen
        alto, ancho = imagen.shape[:2]
        
        # Imprimir el tamaño de la imagen
        # print(f"Tamaño de la imagen '{archivo}': {ancho}x{alto}")
        
        lista_alto.append(alto)
        lista_ancho.append(ancho)
        
import matplotlib.pyplot as plt


# Crear el gráfico de dispersión
plt.scatter(lista_alto,lista_ancho)

# Personalizar el gráfico (opcional)
plt.title('Gráfico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()