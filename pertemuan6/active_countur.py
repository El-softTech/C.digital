import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters import gaussian
from skimage.segmentation import active_contour

# Baca gambar
img = io.imread('image.png')
img_gray = color.rgb2gray(img)

# Smooth image
img_smooth = gaussian(img_gray, 1)

# Initial snake (initial contour)
s = np.linspace(0, 2 * np.pi, 400)
x = 200 + 100 * np.cos(s)
y = 100 + 100 * np.sin(s)
init = np.array([x, y]).T

# Active contour model
snake = active_contour(img_smooth, init, alpha=0.015, beta=10, gamma=0.001)

# Plot the results
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap='gray')
ax.plot(init[:, 0], init[:, 1], '--r', lw=3, label='Initial Contour')
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3, label='Active Contour')
ax.set_title('Active Contour Segmentation')
ax.axis('off')
ax.legend()
plt.show()
