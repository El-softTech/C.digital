import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('threshold.jpg', cv2.IMREAD_GRAYSCALE)


_, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(img, cmap='gray')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.title("Otsu's Thresholding")
plt.imshow(otsu_thresh, cmap='gray')
plt.axis('off')

plt.show()
