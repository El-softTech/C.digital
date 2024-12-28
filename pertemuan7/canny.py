import cv2
import numpy as np
import matplotlib.pyplot as plt


image_color = cv2.imread('pohon.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(image_gray, 100, 200)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Deteksi Tepi Canny')
plt.axis('off')

plt.show()
