import numpy as np
import imutils
import cv2

image = cv2.imread(r'images\hat_cat.jpg')


# #### MÉTODO "WARP AFFINE" ####

# # MATRIZ DE DESLOCAMENTO. ESQUERDA OU DIREITA | ACIMA OU ABAIXO
# # [1, 0, Tx], ONDE "Tx" É O NÚMERO DE PIXELS A SER MOVIDO PARA DIREITA OU ESQUERDA
# # VALORES POSITIVOS = MOVER PARA A DIREITA
# # VALORES NEGATIVOS = ESQUERDA

# # [0,  1, Ty], ONDE "Ty" É O NÚMERO DE PIXELS A SER MOVIDO PARA CIMA OU BAIXO
# # VALORES POSITIVOS = MOVER PARA BAIXO
# # VALORES NEGATIVOS = CIMA
# M = np.float32([[1, 0, 25], [0, 1, 50]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow('Baixo e direita', shifted)

# M = np.float32([[1, 0, -50], [0, 1, -90]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow('Acima e esquerda', shifted)


# #### IMUTILS ####
# def translate(image, x, y):
#     M = np.float32([[1, 0, x], [0, 1, y]])
#     shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#     return shifted
# shifted = translate(image, 0, 100)
# cv2.imshow('SHIFTED', shifted)

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
