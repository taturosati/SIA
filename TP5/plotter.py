import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# points
# [[x=1, y=2], [x=3, y=4], [x=5, y=6]]

def scatter_plot(points, labels):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.scatter(x, y)
    plt.show()

def plot_heatmap(matrix, title, labels=None):
    # Create a dataset
    df = pd.DataFrame(matrix)

    # Default heatmap
    p = sns.heatmap(df, annot=labels, fmt='')
    p.set_title(title)

    plt.show()
