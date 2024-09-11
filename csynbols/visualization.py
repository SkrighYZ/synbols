from matplotlib import pyplot as plt

from .utils import make_img_grid
import numpy as np


def plot_dataset(x, y, h_axis="char", v_axis="font", n_row=20, n_col=40, hide_axis=False):
    img_grid, h_values, v_values = make_img_grid(x, y, h_axis, v_axis, n_row, n_col)

    img_grid = np.stack([img_grid[:, :, 2], img_grid[:, :, 1], img_grid[:, :, 0]]).transpose(1, 2, 0)

    plt.tight_layout()

    plt.imshow(img_grid)

    plt.xlabel(h_axis)
    plt.ylabel(v_axis)

    if hide_axis:
        ax = plt.gca()

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.gcf().tight_layout()
    return h_values, v_values
