import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
# file = open('dissolveO2.csv')
# csvreader = csv.reader(file)
# header = next(csvreader)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
df = pd.read_csv('dissolveO2.csv').to_numpy()
T = df[:, 0]
S1 = df[:, 1]
S2 = df[:, 2]
plt.plot(T, S1)
plt.plot(T, S2)
v = int(input())
plt.plot([v, v], [0, S2[0]])
plt.show()
