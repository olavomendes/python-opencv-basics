import numpy as np
import imutils
import cv2


image = cv2.imread(r'images\fat_cat.jpg')

#### ROTAÇÃO ####
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# 45 GRAUS
# 1.0 = MANTER AS DIMENSÕES ORIGINAIS DA IMAGEM | 2.0 = DOBRARIA AS DIMENSÕES | POR AÍ VAI
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotacao de 45 graus', rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)  # -90 GRAUS
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotacao de -90 graus', rotated)


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


rotated = rotate(image, 180)
cv2.imshow('Rotacao de 180 graus', rotated)


cv2.imshow('Original', image)
cv2.waitKey(0)
