import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math


# points
# [[x=1, y=2], [x=3, y=4], [x=5, y=6]]

def scatter_plot(points, labels):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.scatter(x, y)
    for i, label in enumerate(labels):
        plt.annotate(label, (x[i], y[i])) 
        
    plt.title("Espacio latente 2D")
    plt.show()

def plot_heatmap(matrix, title, labels=None):
    # Create a dataset
    df = pd.DataFrame(matrix)

    # Default heatmap
    p = sns.heatmap(df, annot=labels, fmt='', cmap='Blues')
    p.set_title(title)

    plt.show()

# def plot_multiple_heatmaps(matrices, rows, cols):
#     plt.subplots(rows, cols)
#     for i, matrix in enumerate(matrices):
#         df = pd.DataFrame(matrix)
#         if i % 2 == 0:
#             title = "Input"
#         else:
#             title = "Decoded value"
#         p = sns.heatmap(df, fmt='', cmap='Blues')
#         p.set_title(title)
#     plt.show()


def plot_multiple_heatmaps(data,cols):
    rows = math.ceil(len(data) / cols)
    plt.clf()
    plt.figure(layout="constrained")
    fig, axes = plt.subplots(rows, cols)
    # fig.subtitle(title)
    [axi.set_axis_off() for axi in axes.ravel()]
    for i in range(len(data)):
        row = math.floor(i / cols)
        col = i % cols
        sns.heatmap(ax=axes[row, col] if rows > 1 else axes[col], data=data[i], cmap='Blues')
    
    plt.show()