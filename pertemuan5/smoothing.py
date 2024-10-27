import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('image.png')


mean_blur = cv2.blur(image, (5, 5))
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Citra Asli')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title('Perataan (Rata-rata)')
plt.imshow(cv2.cvtColor(mean_blur, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title('Perataan (Gaussian)')
plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()
