import matplotlib.pyplot as plt
import cv2
import numpy as np


image = cv2.imread(r'images\beach.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', image)

#### GRAYSCALE ####

# IMAGE, CHANNELS MASK, HISTSIZE, RANGE
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure(figsize=(5, 3))
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.tight_layout()
plt.show()


cv2.waitKey(0)
