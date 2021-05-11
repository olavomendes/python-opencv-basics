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
# -1 DESENHA TODOS OS CONTORNOS
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)

for i, c in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print('Moeda #{}'.format(i + 1))
    coin = image[y:y + h, x:x+w]
    cv2.imshow('Coin', coin)

    mask = np.zeros(image.shape[:2], dtype='uint8')
    ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]

    cv2.imshow('Masked Coin', cv2.bitwise_and(coin, coin, mask=mask))


cv2.imshow('Image', blurred)
cv2.imshow('Edges', edged)
cv2.imshow('Coins', coins)

cv2.waitKey(0)
