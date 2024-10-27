import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('image.png',0)
filter_img=cv2.medianBlur(image,5)


plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(image,cmap='gray')  


plt.subplot(1, 2, 2)
plt.title('median filtering')
plt.imshow(filter_img,cmap='gray')
plt.axis("off")


plt.show()
