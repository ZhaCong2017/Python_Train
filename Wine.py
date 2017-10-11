import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# def distance(a, b):
#     dis = 0
#     for i in range(len(a)):
#         dis = dis + (a[i] - b[i]) * (a[i] - b[i])
#     return np.sqrt(dis)
#
# def equal(a, b):
#     x = len(a)
#     y = len(a[0])
#     for i in range(x):
#         for j in range(y):
#             if a[i][j] != b[i][j]:
#                 return False
#     return True

data = np.loadtxt('wine.txt')
type = data[:, 0]
data = data[:, 1:]
# print data.shape

n, L = data.shape
k = 3

max = np.zeros(L)
for i in range(L):
    for j in range(n):
        if max[i] < data[j][i]:
            max[i] = data[j][i]

# print data[0]
for i in range(n):
    data[i] = data[i] / max


km = KMeans(n_clusters=3)
label = km.fit_predict(data)
print km.cluster_centers_
expenses = np.sum(km.cluster_centers_, axis=1)
# print expenses
WineCluster = [[] for i in range(k)]
for i in range(len(type)):
    WineCluster[label[i]].append(type[i])
for i in range(len(WineCluster)):
    # print("Expenses:%.2f" % expenses[i])
    # print(WineCluster[i])
    tmp = np.zeros(3)
    for j in range(len(WineCluster[i])):
        tmp[int(WineCluster[i][j]) - 1] += 1
    print tmp

# print L

# center = np.zeros((k, L))
# newcenter = np.zeros((k, L))
# for i in range(k):
#     tmp = random.randint(0, n)
#     for j in range(L):
#         newcenter[i][j] = data[tmp][j]
#
# it = 0
# while not equal(center, newcenter):
#     center = newcenter
#     newcenter = np.zeros((k, L))
#     num = np.zeros(k)
#     for i in range(n):
#         minist = []
#         for j in range(k):
#             minist.append(distance(center[j], data[i]))
#         place = minist.index(min(minist))
#         num[place] += 1
#         newcenter[place] += data[i]
#     for i in range(k):
#         tmp = num[i]
#         newcenter[i] = newcenter[i] / tmp
#
#     it += 1
#     if it % 1 == 0:
#         print it
#
#
# num = np.zeros((k, k))
# for i in range(n):
#     minist = []
#     for j in range(k):
#         minist.append(distance(center[j], data[i]))
#     place = minist.index(min(minist))
#     num[int(type[i] - 1)][place] += 1
#
# print num

