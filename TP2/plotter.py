import numpy as np
import matplotlib.pyplot as plt


def plot(arr: dict, title: str):

    x = np.array(range(len(arr["max"])))

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")

    ax.set_xlabel("gen n")
    ax.set_ylabel("fitness")
    ax.locator_params("y", nbins=10)
    ax.locator_params("x", nbins=15)
    ax.plot(x, arr["max"], label="max", color="r")
    ax.plot(x, arr["avg"], label="avg", color="b")
    ax.set_title(title)
    ax.legend()
    plt.show()
