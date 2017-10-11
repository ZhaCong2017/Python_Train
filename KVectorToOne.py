import random
import sys
import time


class item:
    def __init__(self, a, b, c):
        self.num = a
        self.place = b
        self.position = c


def left(x):
    return x * 2


def right(x):
    return x * 2 + 1


def minheapify(num, k):
    n = len(num)
    k += 1
    l = left(k)
    r = right(k)
    minest = k
    if l <= n and num[l - 1].num < num[k - 1].num:
        minest = l
    if r <= n and num[minest - 1].num > num[r - 1].num:
        minest = r
    if minest != k:
        tmp = num[minest - 1]
        num[minest - 1] = num[k - 1]
        num[k - 1] = tmp
        minheapify(num, minest - 1)


def buildheap(heap):
    i = len(heap) / 2
    while i >= 0:
        minheapify(heap, i)
        i -= 1

k = 15
n = 200000
num = [[] for i in range(k)]
for i in range(k):
    for j in range(n):
        num[i].append(random.randint(0, 100 * n))
    num[i].sort()
result = []
heap = []

start = time.clock()
for i in range(k):
    heap.append(item(num[i][0], i, 0))
buildheap(heap)

i = 0
while i < n * k:
    result.append(heap[0].num)
    if heap[0].position + 1 < n:
        tmp = item(num[heap[0].place][heap[0].position + 1], heap[0].place, heap[0].position + 1)
    else:
        tmp = item(sys.maxint, heap[0].place, heap[0].position + 1)
    heap[0] = tmp
    minheapify(heap, 0)
    i += 1
end = time.clock()
print end - start
# print num
# print result
print len(result), k * n

for i in range(1, k * n):
    if result[i] < result[i - 1]:
        print "False"

for i in range(k):
    for j in range(n):
        a = 0
        for x in range(k):
            a += num[x].count(num[i][j])
        b = result.count(num[i][j])
        if a != b:
            print "F", a, b, num[i][j]

