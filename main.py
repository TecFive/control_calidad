import numpy as np
import cv2
import os

def compare(i1, i2):
    i2_resized = cv2.resize(i2, (i1.shape[1], i1.shape[0]))
    diferencia = cv2.subtract(i1, i2_resized)
    if not np.any(diferencia):
        print("Perfect")
    else:
        # Calcula el porcentaje de similitud
        porcentaje_similitud = (np.count_nonzero(diferencia == 0) / diferencia.size) * 100
        print(f"Imperfect - Similarity: {porcentaje_similitud:.2f}%")

sample = cv2.imread("Assets/original.png")

for i in range(1, 13):
    tmpimg = cv2.imread(f"Assets/{i}.png")
    compare(sample, tmpimg)
