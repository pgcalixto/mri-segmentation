import scipy.io
import matplotlib.pyplot as plt
import numpy as np

def load_mat_img():
    """Read image data from local MAT file

    Reads local 'vbm.mat' data and returns its array of values.

    Returns:
        numpy.ndarray: Array of values read from MAT file
    """
    # read mat image and normalize it
    mat_data = scipy.io.loadmat('vbm.mat')
    image = mat_data['vbm'] / np.amax(mat_data['vbm'])

    return image

def multi_slice_viewer(image):
    """Display image and set key press event.

    Displays 3D input image data in 2D slice and sets the key press events which
    go forward and backward through slices.

    Args:
        image (numpy.ndarray): tridimensional array of image values
    """
    # saves image in axis data, sets slice index and plots it
    fig, axes = plt.subplots(2, 2)

    for i, j in [(0, 0), (0, 1), (1, 0)]:
        image3d = np.rollaxis(image, 2 * i + j)
        axes[i][j].index = 1
        axes[i][j].imshow(image3d[axes[i][j].index, :, :], vmin=0, vmax=1)
        axes[i][j].image3d = image3d

    axes[-1][-1].axis('off')

    # sets the key event
    fig.canvas.mpl_connect('key_press_event', process_key)
    plt.show()

def process_key(event):
    """Set key actions for the canvas."""
    fig = event.canvas.figure
    if event.key == 'j':
        previous_slice(fig.axes)
    elif event.key == 'k':
        next_slice(fig.axes)
    fig.canvas.draw()

def previous_slice(axes):
    """Go to the previous slice."""
    for i in range(3):
        image3d = axes[i].image3d
         # wrap around using % modulus
        axes[i].index = (axes[i].index - 1) % image3d.shape[0]
        axes[i].images[0].set_array(image3d[axes[i].index, :, :])


def next_slice(axes):
    """Go to the next slice."""
    for i in range(3):
        image3d = axes[i].image3d
         # wrap around using % modulus
        axes[i].index = (axes[i].index - 1) % image3d.shape[0]
        axes[i].images[0].set_array(image3d[axes[i].index, :, :])


def main():
    """Main function.

    This function is responsible for reading a MAT file and displaying its data.
    """
    img = load_mat_img()
    multi_slice_viewer(img)

if __name__ == '__main__':
    main()
