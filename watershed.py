from scipy import ndimage as ndi
import matplotlib.pyplot as plt

from skimage import io
from skimage.morphology import watershed, disk
from skimage import data
from skimage.filter import rank
import cv2

image = io.imread('cerebro.jpg')

# makes the image grey colormap
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# denoise image
denoised = rank.median(gray, disk(1))

# create the sheds
markers = rank.gradient(denoised, disk(1)) < 15
markers = ndi.label(markers)[0]

# process the watershed
labels = watershed(gray, markers)

# display results
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8),
                         sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_title("Original")

ax[1].imshow(gray, cmap=plt.cm.nipy_spectral, interpolation='nearest')
ax[1].set_title("Threshold")

ax[2].imshow(markers, cmap=plt.cm.nipy_spectral, interpolation='nearest')
ax[2].set_title("Markers")

ax[3].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[3].imshow(labels, cmap=plt.cm.nipy_spectral, interpolation='nearest', alpha=.7)
ax[3].set_title("Segmented")

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
