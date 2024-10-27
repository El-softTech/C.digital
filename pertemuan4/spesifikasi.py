import numpy as np
import cv2
import matplotlib.pyplot as plt

def spesifikasi_histogram(sumber, target):
    hist_sumber, _ = np.histogram(sumber.flatten(), 256, [0, 256])
    cdf_sumber = hist_sumber.cumsum()
    cdf_sumber_normalisasi = (255 * cdf_sumber / cdf_sumber[-1]).astype(np.uint8)

    hist_target, _ = np.histogram(target.flatten(), 256, [0, 256])
    cdf_target = hist_target.cumsum()
    cdf_target_normalisasi = (255 * cdf_target / cdf_target[-1]).astype(np.uint8)

    peta_intensitas = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        selisih = np.abs(cdf_target_normalisasi - cdf_sumber_normalisasi[i])
        peta_intensitas[i] = np.argmin(selisih)

    gambar_spesifikasi = peta_intensitas[sumber]

    return gambar_spesifikasi

sumber = cv2.imread("mendung.jpg", 0)
target = cv2.imread("cerah.jpg", 0)

hasil_spesifikasi = spesifikasi_histogram(sumber, target)
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.title("Gambar Asli")
plt.imshow(sumber, cmap="gray")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.title("Gambar Spesifikasi")
plt.imshow(hasil_spesifikasi, cmap="gray")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.title("Histogram Gambar Asli")
plt.hist(sumber.flatten(), bins=256, range=[0, 256], color='black')
plt.xlim([0, 256])
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.subplot(2, 2, 4)
plt.title("Histogram Gambar Spesifikasi")
plt.hist(hasil_spesifikasi.flatten(), bins=256, range=[0, 256], color='black')
plt.xlim([0, 256])
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()
