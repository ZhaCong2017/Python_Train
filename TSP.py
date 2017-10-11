import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import time
import math


def wheelselected(p, active):
    wheel = np.random.rand()
    wheelsum = 0
    for i in range(len(active)):
        wheelsum += p[i]
        if wheelsum >= wheel:
            return active[i]


city = np.loadtxt('input2.txt')
num = city.shape[0]
distance = np.zeros((num, num))
for i in range(num):
    for j in range(i + 1, num):
        distance[i][j] = distance[j][i] = math.sqrt(pow(city[i][0] - city[j][0], 2) + pow(city[i][1] - city[j][1], 2))
antnum = 2 * num
itermax = 180 * num
iter = 0
alpha = 1
beta = 1
rho = 0.36
Q = 1.5
bestlength = []
averlength = []
result = sys.maxint
pheromone = np.ones((num, num)) * 1.5
bestroad = []
# print pheromone
while iter < itermax:
    iter += 1
    start = []
    length = np.zeros(antnum)
    road = np.zeros([antnum, num])
    road[:num, 0] = np.random.permutation(range(0, num))[:]
    road[num:, 0] = np.random.permutation(range(0, num))[:]
    for i in range(antnum):
        activecity = range(num)
        activecity.remove(road[i][0])
        for k in range(num - 1):
            p = np.zeros(len(activecity))
            for j in range(len(activecity)):
                p[j] = pow(pheromone[int(road[i][k])][activecity[j]], alpha) / pow(distance[int(road[i][k])][activecity[j]], beta)
            sump = np.sum(p)
            p = p / sump
            road[i][k + 1] = wheelselected(p, activecity)
            activecity.remove(road[i][k + 1])
        for j in range(num - 1):
            length[i] += distance[int(road[i][j])][int(road[i][j + 1])]
        length[i] += distance[int(road[i][num - 1])][int(road[i][0])]
        if result > length[i]:
            result = length[i]
            bestroad = road[i]
    if min(length) < result:
        bestlength.append(min(length))
    else:
        bestlength.append(result)
    averlength.append(length.mean())
    # print averlength
    changpheromone = np.zeros((num, num))
    for i in range(antnum):
        for j in range(num - 1):
            changpheromone[int(road[i][j])][int(road[i][j + 1])] += Q / distance[int(road[i][j])][int(road[i][j + 1])]
        changpheromone[int(road[i][num - 1])][int(road[i][0])] += Q / distance[int(road[i][num - 1])][int(road[i][0])]

    pheromone = (1 - rho) * pheromone + changpheromone

    iter += 1
    if iter % 100 == 0:
        print iter
        print result
        print bestroad

print result
print averlength
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
axes[0].plot(averlength, 'k', marker = u'')
axes[0].set_title('Average Length')
axes[0].set_xlabel(u'iteration')

axes[1].plot(bestlength, 'k', marker = u'')
axes[1].set_title('Best Length')
axes[1].set_xlabel(u'iteration')
fig.savefig('Average_Best.png', dpi=500, bbox_inches='tight')
plt.show()


plt.plot(city[:, 0], city[:, 1], 'r.', marker=u'$\cdot$')
plt.xlim([min(city[:, 0]) - 1, max(city[:, 0]) + 1])
plt.ylim([min(city[:, 1]) - 1, max(city[:, 1]) + 1])

for i in range(num - 1):
    m = int(bestroad[i])
    n = int(bestroad[i+1])
    print m, n
    plt.plot([city[m][0], city[n][0]], [city[m][1], city[n][1]], 'k')
plt.plot([city[int(bestroad[0])][0], city[n][0]], [city[int(bestroad[0])][1], city[n][1]], 'b')

ax = plt.gca()
ax.set_title("Best Path")
ax.set_xlabel('X axis')
ax.set_ylabel('Y_axis')

plt.savefig('Best Path.png', dpi=500, bbox_inches='tight')
plt.show()



