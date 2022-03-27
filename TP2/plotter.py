from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# x1 = [1,2,3,4,5]
# y1 = [3,5,4,7,3]
# x2 = [1,2,3,4,5]
# y2 = [2,4,3,5,3]

# # plot lines
# plt.plot(x1, y1, label = "max")
# plt.plot(x2, y2, label = "avg")
# plt.legend()
# plt.show()


def plot(arr: dict):

    x = np.array(range(len(arr["max"])))

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")

    ax.set_xlabel("gen n")
    ax.set_ylabel("fitness")
    ax.locator_params("y", nbins=10)
    ax.locator_params("x", nbins=15)
    ax.plot(x, arr["max"], label="max", color="r")
    ax.plot(x, arr["avg"], label="avg", color="b")
    ax.set_title("Max vs Avg")
    ax.legend()
    plt.show()
