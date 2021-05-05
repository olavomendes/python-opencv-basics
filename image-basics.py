import cv2

image = cv2.imread(r'images\hat_cat.png')
cv2.imshow('Original image', image)

(b, g, r) = image[0, 0]  # BRG
print('Pixel (0, 0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print('Pixel (0, 0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

corner = image[0:100, 0:100]  # Y INICIAL:Y FINAL | X INICIAL:X FINAL
cv2.imshow('Corner', corner)
image[0:100, 0:300] = (0, 255, 0)
cv2.imshow('Updated', image)

cv2.waitKey(0)
