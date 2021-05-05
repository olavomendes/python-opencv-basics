import numpy as np
import cv2

# 300 linhas, 300 colunas, 3 canais
canvas = np.zeros((300, 300, 3), dtype='uint8')
cv2.imshow('Canvas', canvas)


##### LINHAS ####
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow('Canvas', canvas)

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow('Canvas', canvas)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow('Canvas', canvas)

##### RETÂNGULOS ####
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow('Canvas', canvas)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow('Canvas', canvas)

blue = (255, 0, 0)
# THICKNESS NEGATIVA = RETÂGULO CHEIO
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow('Canvas', canvas)

##### CÍRCULOS ####
canvas = np.zeros((300, 300, 3), dtype='uint8')
# COORDENADAS DO CENTRO DA IMAGEM
(center_x, center_y) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
for r in range(0, 175, 25):  # r = RAIO
    cv2.circle(canvas, (center_x, center_y), r, white)
cv2.imshow('Canvas', canvas)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    # RETORNA UMA LISTA COM 3 NÚMEROS
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow('Canvas', canvas)

cv2.waitKey(0)
