import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)


threshold_value = 140


_, thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(img, cmap='gray')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.title('Global Thresholding')
plt.imshow(thresholded_img, cmap='gray')
plt.axis('off')

plt.show()
