import cv2
import numpy as np
import matplotlib.pyplot as plt


image_color = cv2.imread('pohon.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)


sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobel_x**2 + sobel_y**2)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel, cmap='gray')
plt.title('Deteksi Tepi Sobel')
plt.axis('off')

plt.show()
