import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('bunga.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 


hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


lower_color = np.array([10, 20, 20])  
upper_color = np.array([70, 255, 255])  


mask = cv2.inRange(hsv_image, lower_color, upper_color)


result = cv2.bitwise_and(image, image, mask=mask)


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Masker')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(result)
plt.title('Hasil Segmentasi')
plt.axis('off')

plt.show()
