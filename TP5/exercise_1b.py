from plotter import plot_multiple_heatmaps
from utils import Utils
from denoising_autoencoder import DenoisingAutoencoder
import numpy as np
from fonts import font_2

font = np.array([np.array(Utils.to_bin_array(c)).flatten() for c in font_2])

font_subset = font[1:9]
print("Primeras", len(font_subset), "letras")
font_labels = [chr(0x41 + i) for i in range(len(font_subset))]

prob = 0.1
max_noise = 0.3
print("Mutation prob:", prob)
print("Max noise:", max_noise)

layers = [35, 25, 10, 12, 5, 12, 10, 25, 35]
dae = DenoisingAutoencoder(layers, 35, prob, max_noise)

print("Capas: ", layers)
dae.solve({"in": font_subset, "out": font_subset})

data = []
for c in font_subset:
    noisy_input = Utils.noise_pattern(c, prob, max_noise)

    output = dae.output(noisy_input)
    
    output.resize((7, 5))
    noisy_input.resize((7, 5))
    data.append(noisy_input)
    data.append(output)

plot_multiple_heatmaps(data, 8)



