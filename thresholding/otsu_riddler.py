import cv2
import numpy as np
import mahotas

image = cv2.imread(r'images\coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

T = mahotas.thresholding.otsu(blurred)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Otsu', thresh)

T = mahotas.thresholding.rc(blurred)

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Riddler-Calvard', thresh)


cv2.imshow('Original', image)
cv2.waitKey(0)
