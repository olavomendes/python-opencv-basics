# ENVOLVE REMOVER O "NOISE" USANDO "BLUR", COMPUTAR OS GRADIENTES
# X E Y, SUPRIMIR BORDAS E FINALMENTE CALCULAR A LIMINAR

import numpy as np
import cv2

image = cv2.imread(r'images\coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)

canny = cv2.Canny(image, 30, 150)

cv2.imshow('Blurred', image)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
