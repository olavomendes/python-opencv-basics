#### BITWISE OPERATIONS: AND, OR, XOR and NOT ####
# O PIXEL É "LIGADO" SE O VALOR FOR MAIOR QUE ZERO
# E "DESLIGADO" SE FOR ZERO

import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype='uint8')
rectangle = cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow('RETANGULO', rectangle)

circle = np.zeros((300, 300), dtype='uint8')
circle = cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow('CIRCLE', circle)


# É VERDADEIRO SOMENTE SE AMBOS OS PIXELS FOREM MAIORES QUE ZERO
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND', bitwiseAnd)

# É VERDADEIRO SOMENTE SE PELO MENOS UM DOS PIXELS FOREM MAIORES QUE ZERO
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow('OR', bitwiseOr)

# É VERDADEIRO SOMENTE SE PELO MENOS UM DOS PIXELS FOREM MAIORES QUE ZERO
# MAS NÃO AMBOS
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('XOR', bitwiseXor)


# INVERTE O "LIGADO" E "DESLIGADO"
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('NOT', bitwiseNot)


cv2.waitKey(0)
