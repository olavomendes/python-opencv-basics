import numpy as np
import cv2

###  RGB ####
image = cv2.imread(r'images\wave.png')
cv2.imshow('Original', image)

(B, G, R) = cv2.split(image)
cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)

merged = cv2.merge([B, G, R])
# merged = cv2.merge([R, G, B])
cv2.imshow('Merged', merged)


#### OUTROS ESPAÇOS DE CORES ####
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('Lab', lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
