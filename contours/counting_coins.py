import numpy as np
import cv2

image = cv2.imread(r'images\coins.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

edged = cv2.Canny(blurred, 30, 150)

(cnts, hierarchy) = cv2.findContours(edged.copy(),
                                     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Quantidade de moedas na imagem: ', len(cnts))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)


cv2.imshow('Image', blurred)
cv2.imshow('Edges', edged)
cv2.imshow('Coins', coins)

cv2.waitKey(0)
