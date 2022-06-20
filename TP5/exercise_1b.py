from plotter import plot_heatmap
from utils import Utils
from denoising_autoencoder import DenoisingAutoencoder
import numpy as np
from fonts import font_2

font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_2])
for i in range(len(font)):
    for j in range(len(font[i])):
        if font[i][j] == 0:
            font[i][j] = -1

font_subset = font[:5]

dae = DenoisingAutoencoder([35, 18, 25, 10, 25, 18, 35], 35)
dae.solve({"in": font_subset, "out": font_subset})

for c in font_subset:
    noisy_input = np.copy(c)
    for i in range(len(noisy_input)):
        if np.random.uniform() < 0.005:
            noisy_input[i] = 0 if noisy_input[i] == 1 else 1

    output = dae.output(noisy_input)
    for i in range(len(output)):
        output[i] = 1 if output[i] >= 0 else 0
    
    output.resize((7, 5))
    noisy_input.resize((7, 5))
    plot_heatmap(noisy_input, "input")
    plot_heatmap(output, "output")



