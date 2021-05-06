import numpy as np
import imutils
import cv2

image = cv2.imread(r'images\fat_cat.jpg')
image = imutils.resize(image, 300)
cv2.imshow('ORIGINAL', image)

flipped = cv2.flip(image, 1)  # 1 = HORIZONTALMENTE
cv2.imshow('FLIPADA HORIZONTALMENTE', flipped)

flipped = cv2.flip(image, 0)  # 0 = VERTICALMENTE
cv2.imshow('FLIPADA VERTICALMENTE', flipped)

flipped = cv2.flip(image, -1)  # -1 AMBOS
cv2.imshow('FLIPADA HORIZONTALMENTE E VERTICALMENTE', flipped)

cv2.waitKey(0)
