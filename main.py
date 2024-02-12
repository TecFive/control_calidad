import numpy as np
import cv2
import os

def compare(i1,i2):
    diferencia = cv2.subtract(i1,i2) 
    
    if not np.any(diferencia):
        print("Good quality") 
    else:
        print("Bad quality")

sample = cv2.imread("Assets/original.png")

for i in range(1,13):
    tmpimg = cv2.imread(f"Assets/{i}.png")
    compare(sample,tmpimg)