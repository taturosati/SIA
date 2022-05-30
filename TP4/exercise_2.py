import json
import numpy as np
from sympy import unflatten
from plotter import plot_heatmap
from hopfield_network import HopfieldNetwork
import math

def exercise_2(params):
    with open('letters.json', "r") as letters_file:
        patterns = json.load(letters_file)
        letters_file.close()
    unflatten_pat = np.array(patterns)
    patterns = np.array([np.array(pattern).flatten() for pattern in patterns])
    best = []
    min_dist = math.inf
    for i in range(len(patterns) - 3):
        for j in range(i+1, len(patterns) - 2):
            i_j = np.dot(patterns[i], patterns[j])
            for k in range(j+1, len(patterns) - 1):
                i_k = np.dot(patterns[i], patterns[k])
                j_k = np.dot(patterns[j], patterns[k]) 
                for l in range(k+1, len(patterns)):
                    i_l = np.dot(patterns[i], patterns[l])
                    j_l = np.dot(patterns[j], patterns[l])
                    k_l = np.dot(patterns[k], patterns[l])
                    dist = sum([i_j, i_k, j_k, i_l, j_l, k_l])
                    if dist < min_dist:
                        min_dist = dist
                        best = [i, j, k, l]

    for lett in best:
        plot_heatmap(unflatten_pat[lett]*-1, "")

    print([chr(ord('A') + i) for i in best])
    patterns = [patterns[i] for i in best]
    network = HopfieldNetwork(size=25, patterns=patterns)

    noisy_patterns = np.copy(patterns)
    for i in range(len(noisy_patterns)):
        for j in range(len(noisy_patterns[i])):
            if np.random.rand() < params["noise"]:
                noisy_patterns[i][j] = -noisy_patterns[i][j]

    res, historic = network.solve(noisy_patterns[3])
    for idx, his in enumerate(historic):
        print("Paso", idx, ":")
        plot_heatmap(his.reshape(5, 5) * -1, "Paso " + str(idx))

    noisy_p = patterns[0]
    for i in range(len(noisy_p)):
        if np.random.rand() < params["spurius_noise"]:
            noisy_p[i] = -noisy_p[i]

    res, historic = network.solve(noisy_p)

    for idx, his in enumerate(historic):
        print("Paso", idx, ":")
        plot_heatmap(his.reshape(5, 5) * -1, "Paso " + str(idx))

