import numpy as np
import cv2

# 300 linhas, 300 colunas, 3 canais
canvas = np.zeros((300, 300, 3), dtype='uint8')
green = (0, 255, 0)

cv2.imshow('Canvas', canvas)

cv2.waitKey(0)
