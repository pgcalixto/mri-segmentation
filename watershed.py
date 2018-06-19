from scipy import ndimage as ndi
import matplotlib.pyplot as plt

from skimage import io
from skimage.morphology import watershed, disk
from skimage import data
from skimage.filter import rank
import cv2

image = io.imread('cerebro.jpg')

shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# find continuous region (low gradient -
# where less than 10 for this image) --> markers
# disk(5) is used here to get a more smooth image
markers = rank.gradient(thresh, disk(2)) < 10
markers = ndi.label(markers)[0]

# process the watershed
labels = watershed(thresh, markers)

# display results
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8),
                         sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_title("Original")

ax[1].imshow(thresh, cmap=plt.cm.nipy_spectral, interpolation='nearest')
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
