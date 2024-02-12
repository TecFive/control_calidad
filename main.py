import numpy as np
import cv2
import os

sample = cv2.imread("original.png")

for i in range(1,13):
    tmpimg = cv2.imread("{i}.png")
    