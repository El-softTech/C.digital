import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('bunga.jpg', cv2.IMREAD_GRAYSCALE)


prewitt_x = cv2.filter2D(image, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(image, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(prewitt, cmap='gray')
plt.title('Deteksi Tepi Prewitt')
plt.axis('off')

plt.show()
