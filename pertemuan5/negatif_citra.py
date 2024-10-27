import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('image.png')


inverted_image = 255 - image

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('citra asli')
plt.imshow(image,cmap='gray')
plt.axis("off")

plt.subplot(1,2,2)
plt.title('negatif citra')
plt.imshow(inverted_image,cmap='gray')
plt.axis("off")

plt.show()