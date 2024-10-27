import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('image.png')

c=255/np.log(1 * np.max(image))

log_transform =c * (np.log(1 + image))

log_transform =np.array(log_transform, dtype=np.uint8)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('citra asli')
plt.imshow(image,cmap='gray')
plt.axis("off")

plt.subplot(1,2,2)
plt.title('transformasi logaritma')
plt.imshow(log_transform,cmap='gray')
plt.axis("off")

plt.show()