import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


image = cv2.imread('bunga.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)


k = 3


kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
kmeans.fit(pixel_values)


centers = np.uint8(kmeans.cluster_centers_)
labels = kmeans.labels_
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.axis('off')
plt.show()

