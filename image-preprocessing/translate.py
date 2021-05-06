import numpy as np
import imutils
import cv2

image = cv2.imread(r'images\hat_cat.jpg')


#### MÉTODO "WARP AFFINE" ####

# MATRIZ DE DESLOCAMENTO. ESQUERDA OU DIREITA | ACIMA OU ABAIXO
# [1, 0, Tx], ONDE "Tx" É O NÚMERO DE PIXELS A SER MOVIDO PARA DIREITA OU ESQUERDA
# VALORES POSITIVOS = MOVER PARA A DIREITA
# VALORES NEGATIVOS = ESQUERDA

# [0,  1, Ty], ONDE "Ty" É O NÚMERO DE PIXELS A SER MOVIDO PARA CIMA OU BAIXO
# VALORES POSITIVOS = MOVER PARA BAIXO
# VALORES NEGATIVOS = CIMA
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Baixo e direita', shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Acima e esquerda', shifted)


#### IMUTILS ####
def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted


shifted = translate(image, 0, 100)
cv2.imshow('SHIFTED', shifted)


cv2.waitKey(0)
