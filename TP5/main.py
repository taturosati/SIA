import numpy as np

from utils import Utils
from multilayer import Multilayer
from fonts import font_1


font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_1])
print(font[1]);


Multilayer([35, 17, 10, 17, 35], 35, 0.05).solve({"in": font, "out": font}, {"in": [], "out": []}, 0.01)
