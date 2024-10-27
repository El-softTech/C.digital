import cv2
import numpy as np
import matplotlib.pyplot as plt

image_sumber = cv2.imread('mendung.jpg', 0)
histogram_img_sumber, batasan_img_sumber = np.histogram(image_sumber.flatten(), 256, [0, 256])
gambar_ekualisasi = cv2.equalizeHist(image_sumber)
histogram_img_ekualisasi, batasan_img_ekualisasi = np.histogram(gambar_ekualisasi.flatten(), 256, [0, 256])

plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1)
plt.imshow(image_sumber, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(2, 2, 2)
plt.plot(histogram_img_sumber)
plt.title('Histogram Gambar Asli')

plt.subplot(2, 2, 3)
plt.imshow(gambar_ekualisasi, cmap='gray')
plt.title('Gambar Hasil Ekualisasi')

plt.subplot(2, 2, 4)
plt.plot(histogram_img_ekualisasi)
plt.title('Histogram Gambar Hasil Ekualisasi')

plt.tight_layout()
plt.show()
