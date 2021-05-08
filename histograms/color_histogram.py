import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread(r'images\beach.png')

### COLOR ####
cv2.imshow('Original', image)

channels = cv2.split(image)
# colors = ('b', 'g', 'r')
# plt.figure(figsize=(6, 4))
# plt.title('Flattened color histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')

# for (channel, color) in zip(channels, colors):
#     hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
#     plt.plot(hist, color=color)
#     plt.xlim([0, 256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist(channels[1], channels[0], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('2D color histogram for G and B')
plt.colorbar(p)

plt.tight_layout()
plt.show()
cv2.waitKey(0)
