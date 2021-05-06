import numpy as np
import imutils
import cv2

image = cv2.imread(r'images\fat_cat.jpg')
cv2.imshow('ORIGINAL', image)

r = 150.0 / image.shape[1]  # ASPECT RATIO
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Redimensionada (largura)', resized)

r = 50.0 / image.shape[0]  # ASPECT RATIO
dim = (int(image.shape[1] * r), 50)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Redimensionada (altura)', resized)

#### IMUTILS ####

resized = imutils.resize(image, width=400)
cv2.imshow('Redimensionada (imutils)', resized)

cv2.waitKey(0)
