import cv2
import numpy as np

# image = cv2.imread(r'images\trex.png')
image = cv2.imread(r'images\beach.png')

cv2.imshow('Original', image)

#### AVERAGING ####
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])
cv2.imshow('Averaged', blurred)

#### GAUSSIAN ####
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),  # 0 = STD
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])
cv2.imshow('Gaussian', blurred)

#### MEDIAN ####
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])
cv2.imshow('Median', blurred)

#### BILATERAL ####
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow('Bilateral', blurred)

cv2.waitKey(0)
