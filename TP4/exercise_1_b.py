import csv
import numpy as np
from sklearn.preprocessing import StandardScaler
from pca_function import pca_function

from oja_rule import OjaRule

def exercise_1_b(params):
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

        weights = OjaRule(eta=params['eta'], limit=params['limit']).solve(rows)
        pca_component = pca_function()
        # pca_component = np.array([0.124874, -0.500506, 0.406518, -0.482873, 0.188112, -0.475704, 0.271656])
        print(np.linalg.norm(weights - pca_component))
        print(weights)
        
