# UM SIMPLES EXEMPLO É SELECIONAR UM PIXEL COM VALOR "P" E MODIFICAR TODOS OS PIXELS
# MENOS QUE "P" PARA ZERO, E TODOS OS PIXELS MAIORES QUE "P" PARA 255

import numpy as np
import cv2


image = cv2.imread(r'images\coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Original', image)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholding binary', thresh)

(T, thresh_inverse) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresholding binary inverse', thresh_inverse)

cv2.imshow('Coins', cv2.bitwise_and(image, image, mask=thresh_inverse))

cv2.waitKey(0)
