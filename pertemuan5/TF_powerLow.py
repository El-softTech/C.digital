import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.png', 0)

def gamma_correction(image,gamma):
    image_float= image/ 255.0
    corrected_image=np.power(image_float,gamma)
    corrected_image=np.uint8(corrected_image * 255)
    return corrected_image

gamma= 2.2
corected_img= gamma_correction(image,gamma)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title('Transformasi Power-Law (Gamma)'.format(gamma))
plt.imshow(corected_img, cmap='gray')
plt.axis("off")

plt.show()
