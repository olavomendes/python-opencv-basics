# EM UM SISTEMA DE RECONHECIMENTO DE FACES AS PARTES QUE INTERESSAM SÃO AS FACES
# ENTÃO DEVEMOS CONSTRUIR UMA "MÁSCARA" QUE MOSTRE APENAS AS FACES DA IMAGEM

import numpy as np
import cv2

image = cv2.imread(r'images\beach.png')
cv2.imshow('ORIGINAL', image)

mask = np.zeros(image.shape[:2], dtype='uint8')
(c_x, c_y) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (c_x-75, c_y-75), (c_x+75, c_y+75), 255, -1)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mask applied', masked)

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(mask, (c_x, c_y), 100, 255, -1)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mask applied', masked)

cv2.waitKey(0)
