import cv2
import numpy as np

image = cv2.imread(r'images\hat_cat.jpg')
cv2.imshow('Original', image)

print('Max de 255: {}'.format(cv2.add(np.uint8([200]), np.uint8([100]))))
print('Min de 0: {}'.format(cv2.subtract(np.uint8([200]), np.uint8([100]))))

print('\n')

print('Wrap around: {}'.format(np.uint8([200]) + np.uint8([100])))
print('Wrap around: {}'.format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype='uint8') * 100  # ADICIONADO 100 EM CADA PIXEL
added = cv2.add(image, M)
cv2.imshow('ADDED', added)

M = np.ones(image.shape, dtype='uint8') * 100  # REMOVIDO 50 EM CADA PIXEL
subtracted = cv2.subtract(image, M)
cv2.imshow('SUBTRACTED', subtracted)


cv2.waitKey(0)
