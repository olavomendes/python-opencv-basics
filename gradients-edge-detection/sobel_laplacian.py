import numpy as np
import cv2

image = cv2.imread(r'images\coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(image, cv2.CV_64F)  # COMPUTE THE GRADIENT MAGNITUDE
lap = np.uint8(np.absolute(lap))

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)  # EIXO X - VERTICAL
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)  # EIXO Y - HORIZONTAL
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)  # HORIZONTAL E VERTICAL

cv2.imshow('Original', image)
cv2.imshow('Laplacian', lap)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)

cv2.waitKey(0)
