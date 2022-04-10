import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('download.png', 0)
cv2.imshow("original", img)
# img = img / 255
plt.imshow(img, cmap='Greys')
# cv2.waitKey(0)
print(np.shape(img))
print(img)
plt.show()
cv2.waitKey(0)