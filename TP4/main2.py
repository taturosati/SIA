import json
import numpy as np
from hopfield_network import HopfieldNetwork

with open('letters.json', "r") as letters_file:
    patterns = json.load(letters_file)
    letters_file.close()

patterns = np.array([np.array(pattern).flatten() for pattern in patterns])

network = HopfieldNetwork(size=25, patterns=patterns)

noisy_patterns = np.copy(patterns)
for i in range(len(noisy_patterns)):
    for j in range(len(noisy_patterns[i])):
        if np.random.rand() < 0.05:
            noisy_patterns[i][j] = -noisy_patterns[i][j]

# print(noisy_patterns[1])
res = network.solve(noisy_patterns[1])
for i in range(5):
    print(res[5*i: 5*(i+1)])

