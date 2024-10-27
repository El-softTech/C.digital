import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('image.png')
filter_laplacian=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

sharped_image=cv2.filter2D(image,-1,filter_laplacian)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(image,cmap='gray')  
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title('penajaman')
plt.imshow(sharped_image,cmap='gray')
plt.axis("off")


plt.show()
