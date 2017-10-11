import random
import numpy as np

def initcompetition(n, m, d):
    array = random.random(size=n*m*d)
    weight = array.reshape(n, m, d)
    return weight

def normalize(data):
    old_data = np.copy(data)
    for num in
    return data
data = np.loadtxt('wine.txt')
type = data[:, 0]
data = data[:, 1:]
for i in range(m)




n, m = data.shape
print data
print type
