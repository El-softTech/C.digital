import cv2
import numpy as np
import matplotlib.pyplot as plt

image_color = cv2.imread('pohon.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

prewitt_x = cv2.filter2D(image_gray, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(image_gray, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)

hsv_image = cv2.cvtColor(image_color, cv2.COLOR_BGR2HSV)

lower_bounds = [np.array([35, 50, 50]), np.array([0, 50, 50]), np.array([100, 50, 50])]
upper_bounds = [np.array([85, 255, 255]), np.array([10, 255, 255]), np.array([140, 255, 255])]

mask = cv2.inRange(hsv_image, lower_bounds[0], upper_bounds[0])
for i in range(1, len(lower_bounds)):
    mask = cv2.bitwise_or(mask, cv2.inRange(hsv_image, lower_bounds[i], upper_bounds[i]))

segmented_image = cv2.bitwise_and(image_color, image_color, mask=mask)

plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(prewitt, cmap='gray')
plt.title('Deteksi Tepi Prewitt')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmentasi Warna Thresholding')
plt.axis('off')

plt.show()
