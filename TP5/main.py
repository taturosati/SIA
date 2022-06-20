import math
import numpy as np
from plotter import scatter_plot, plot_heatmap, plot_multiple_heatmaps

from utils import Utils
from multilayer import Multilayer
from fonts import font_1, font_2

font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_2])
# C = Utils.to_bin_array(font_2[3])
# for i in range(len(C)):
#     for j in range(len(C[i])):
#         C[i][j] = 1 - C[i][j]

# plot_heatmap(C, "C")
# for i in range(len(font)):
#     for j in range(len(font[i])):
#         if font[i][j] == 0:
#             font[i][j] = -1


font_subset = font[:3]
print("Primeras", len(font_subset), "letras")
font_labels = [chr(0x40 + i) for i in range(len(font_subset))]


network = Multilayer([35, 11, 8, 12, 8, 11, 35], 35)
print("Red: [35, 11, 8, 2, 8, 11, 35]")
network.solve({"in": font_subset, "out": font_subset})

points = []
matrices = []
for c in font_subset:
    latent_output = network.get_latent(c)
    points.append(latent_output)
    # print(latent_output)
    decoded_value = network.output(c)
    decoded_value.resize((7,5))
    input_value = np.copy(c)
    input_value.resize((7,5))
    matrices.append(input_value)
    matrices.append(decoded_value)
    # plot_heatmap(input_value, "Input")
    # plot_heatmap(decoded_value, "Decoded value")

plot_multiple_heatmaps(matrices)

scatter_plot(points, font_labels)

points_x = [p[0] for p in points]
points_y = [p[1] for p in points]

decode_output = network.decode([np.average(points_x), np.average(points_y)])
for i in range(len(decode_output)):
    decode_output[i] = 1 if decode_output[i] >= 0.5 else 0

decode_output.resize((7, 5))

plot_heatmap(decode_output, "New letter")
