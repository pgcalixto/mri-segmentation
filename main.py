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

    axes[0][0].image3d = image
    axes[0][0].index = 1
    axes[0][0].imshow(image[axes[0][0].index, :, :], vmin=0, vmax=1)

    axes[0][1].image3d = image
    axes[0][1].index = 1
    axes[0][1].imshow(image[:, axes[0][1].index, :], vmin=0, vmax=1)

    axes[1][0].image3d = image
    axes[1][0].index = 1
    axes[1][0].imshow(image[:, :, axes[1][0].index], vmin=0, vmax=1)

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
    image3d = axes[0].image3d
    axes[0].index = (axes[0].index - 1) % image3d.shape[0]
    axes[0].images[0].set_array(image3d[axes[0].index, :, :])

    image3d = axes[1].image3d
    axes[1].index = (axes[1].index - 1) % image3d.shape[1] # wrap around using %
    axes[1].images[0].set_array(image3d[:, axes[1].index, :])

    image3d = axes[2].image3d
    axes[2].index = (axes[2].index - 1) % image3d.shape[2] # wrap around using %
    axes[2].images[0].set_array(image3d[:, :, axes[2].index])

def next_slice(axes):
    """Go to the next slice."""
    image3d = axes[0].image3d
    axes[0].index = (axes[0].index + 1) % image3d.shape[0] # wrap around using %
    axes[0].images[0].set_array(image3d[axes[0].index, :, :])

    image3d = axes[1].image3d
    axes[1].index = (axes[1].index + 1) % image3d.shape[1] # wrap around using %
    axes[1].images[0].set_array(image3d[:, axes[1].index, :])

    image3d = axes[2].image3d
    axes[2].index = (axes[2].index + 1) % image3d.shape[2] # wrap around using %
    axes[2].images[0].set_array(image3d[:, :, axes[2].index])


def main():
    """Main function.

    This function is responsible for reading a MAT file and displaying its data.
    """
    img = load_mat_img()
    multi_slice_viewer(img)

if __name__ == '__main__':
    main()
