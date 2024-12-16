import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)


adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 11, 2)


adaptive_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(adaptive_mean, cmap='gray')
plt.title('Adaptive Thresholding (Mean)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(adaptive_gaussian, cmap='gray')
plt.title('Adaptive Thresholding (Gaussian)')
plt.axis('off')

plt.show()
