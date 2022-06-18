import numpy as np

from utils import Utils
from multilayer import Multilayer
from fonts import font_1

font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_1])

network = Multilayer([35, 25, 18, 25, 35], 35)
network.solve({"in": font, "out": font})


