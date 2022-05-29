import csv
import numpy as np
from sklearn.preprocessing import StandardScaler
from kohonen_network import KohonenNetwork
from plotter import plot_heatmap

with open('europe.csv', newline='') as csvfile:
    # create np array with csv rows
    rows = np.array(list(csv.reader(csvfile, delimiter=',')))
    headers = np.array(rows[0][1:])
    rows = rows[1:]  # ignoro headers
    countries = [row[0] for row in rows]  # me quedo con los paises para poner los labels
    rows = np.array([row[1:] for row in rows])  # elimino pais

    rows = rows.astype(float)

    csvfile.close()

    rows = StandardScaler().fit_transform(rows)
    # print("Patterns:")
    # print(rows)

    grid_k = 4

    network = KohonenNetwork(eta=0.1, limit=0.1, grid_k=grid_k, radius=grid_k)

    network.solve(rows)

    winners_associated = np.zeros((grid_k, grid_k))
    winners = network.find_all_winners(rows)
    labels = np.empty(dtype="U256", shape=(grid_k, grid_k))
    for idx, (row, col) in enumerate(winners):
        winners_associated[row][col] += 1
        labels[row][col] += countries[idx] + "\n"
        print(labels[row][col])
        print(countries[idx], end=" ")
        print("(" + str(row) + ", " + str(col) + ")")

    print(winners_associated)
    plot_heatmap(winners_associated, "Solución", labels)
    plot_heatmap(network.u_matrix(), "Matriz U")
