import numpy as np
from matplotlib import pyplot as plt, animation


def plot(inputs, outputs, weights, title: str):
    fig, ax = plt.subplots(figsize=(4, 4), layout="constrained")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.locator_params("y", nbins=10)
    ax.locator_params("x", nbins=10)
    for i in range(len(inputs)):
        color = "red" if outputs[i] == -1 else "blue"
        ax.scatter(inputs[i][1], inputs[i][2], color=color)
    
    x1 = -1.5
    x2 = 1.5
    
    a = -(weights[1][1] / weights[1][2])
    b = (weights[1][0] / weights[1][2])
    f = lambda x: a * x + b
    line, = ax.plot([x1, x2], [f(x1), f(x2)], color="black")

    ax.set_title(title)
    def animate(i):
        a = -(weights[i][1] / weights[i][2])
        b = (weights[i][0] / weights[i][2])
        f = lambda x: a * x + b
        line.set_ydata([f(x1), f(x2)])

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(weights))
    # anim.save(title + str(np.random.uniform()) + ".gif")
    plt.show()

def plot_error(errors):
    x = np.array(range(len(errors)))

    fig, ax = plt.subplots(figsize=(5, 3), layout="constrained")

    ax.set_xlabel("Iteración")
    ax.set_ylabel("Error")
    ax.locator_params("y")
    ax.locator_params("x")
    ax.plot(x, errors, label="Error", color="b")
    ax.set_title("Error por iteración")
    ax.legend()
    plt.show()
