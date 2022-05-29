import csv
import numpy as np
from sklearn.preprocessing import StandardScaler

from oja_rule import OjaRule

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

    weights = OjaRule(eta=0.0001, limit=50000).solve(rows)

    print(weights)
    

    
