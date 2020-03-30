from synbols.data_io import pack_dataset
from synbols.drawing import Camouflage
from synbols.generate import generate_char_grid
from view_dataset import plot_dataset
import synbols
import numpy as np


if __name__ == "__main__":
    alphabet = 'latin'  # TODO missing upper cases
    # alphabet = 'telugu'  # TODO the circle in some chars is not rendered. (bottom ones)
    # alphabet = 'thai'
    # alphabet = 'vietnamese'
    # alphabet = 'arabic'  # TODO: missing chars in fonts
    # alphabet = 'hebrew'
    # alphabet = 'khmer' # TODO: see comment in googlefonts
    # alphabet = 'tamil'
    # alphabet = 'gujarati' # TODO: one font to remove and one blank in another font
    # alphabet = 'bengali'
    # alphabet = 'malayalam'
    # alphabet = 'korean' # TODO: huge amount of missing chars
    # alphabet = 'chinese-simplified'
    # alphabet = 'greek'
    # alphabet = 'cyrillic'

    # bg = synbols.Camouflage(stroke_angle=1.5)
    # bg = synbols.NoPattern()
    bg = synbols.MultiGradient(alpha=0.5, n_gradients=2, types=('linear', 'radial'))
    # bg = synbols.Gradient(types=('linear',), random_color=synbols.color_sampler(brightness_range=(0.1, 0.9)))

    # fg = synbols.Camouflage(stroke_angle=0.5)
    # fg = synbols.SolidColor((1, 0, 0))
    fg = synbols.Gradient(types=('radial',), random_color=synbols.color_sampler(brightness_range=(0.1, 0.9)))
    # fg = synbols.NoPattern()

    # kwargs = dict(foreground=fg, background=bg, is_bold=True, scale=(0.2, 0.2),
    #               resolution=(32, 32), rng=np.random.RandomState(42), n_symbols=20)

    kwargs = dict()

    x, y = pack_dataset(generate_char_grid('latin', n_font=15, n_char=20, **kwargs))
    plot_dataset(x, y, name=alphabet, h_axis='char', v_axis='font', rng=np.random.RandomState(42))
