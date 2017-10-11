import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

data = np.loadtxt('wine.txt')
y = data[:, 0]
X = data[:, 1:]
max = np.zeros(len(X[0]))
for i in range(len(X[0])):
    for j in range(len(y)):
        if max[i] < X[j][i]:
            max[i] = X[j][i]

# print data[0]
for i in range(len(y)):
    X[i] = X[i] / max

pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

for i in range(len(reduced_X)):
    if y[i] == 1:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 2:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()