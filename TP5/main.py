import math
import numpy as np
from plotter import scatter_plot, plot_heatmap

from utils import Utils
from multilayer import Multilayer
from fonts import font_1, font_2

font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_2])
for i in range(len(font)):
    for j in range(len(font[i])):
        if font[i][j] == 0:
            font[i][j] = -1

font_subset = font[:10]

network = Multilayer([35, 5, 2, 5, 35], 35)
network.solve({"in": font_subset, "out": font_subset})

points = []
for c in font_subset:
    latent_output = network.get_latent(c)
    points.append(latent_output)
    print(latent_output)

scatter_plot(points, [])

points_x = [p[0] for p in points]
points_y = [p[1] for p in points]


decode_output = network.decode([np.average(points_x), np.average(points_y)])
print(decode_output)
decode_output.resize((7, 5))
print(decode_output)

plot_heatmap(decode_output, "new letter")
