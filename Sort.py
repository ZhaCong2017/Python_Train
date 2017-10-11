import random
import time
import sys


def QuickSort(num, lo, hi):
    if lo < hi:
        i = lo
        j = hi
        key = num[lo]
        while i < j:
            while i < j and num[j] >= key:
                j -= 1
            num[i] = num[j]
            while i < j and num[i] <= key:
                i += 1
            num[j] = num[i]
        num[i] = key
        QuickSort(num, lo, i - 1)
        QuickSort(num, i + 1, hi)


def Left(x):
    return x * 2


def Right(x):
    return x * 2 + 1


def MaxHeapify(num, n, place):
    place += 1
    left = Left(place)
    right = Right(place)
    largest = place
    if left <= n and num[place - 1] < num[left - 1]:
        largest = left
    else:
        largest = place
    if right <= n and num[largest - 1] < num[right - 1]:
        largest = right
    if largest != place:
        tmp = num[largest - 1]
        num[largest - 1] = num[place - 1]
        num[place - 1] = tmp
        MaxHeapify(num, n, largest - 1)


def MaxHeap(num, n):
    i = n / 2
    while i >= 0:
        MaxHeapify(num, n, i)
        i -= 1


def HeapSort(num):
    MaxHeap(num, len(num))
    i = len(num) - 1
    while i > 0:
        tmp = num[0]
        num[0] = num[i]
        num[i] = tmp
        MaxHeapify(num, i, 0)
        i -= 1


def Merge(num, lo, mid, hi):
    left = []
    right = []
    for i in range(hi - lo + 1):
        if i <= mid:
            left.append(num[i])
        else:
            right.append(num[i])
    left.append(sys.maxint)
    right.append(sys.maxint)
    i = 0
    j = 0
    k = lo
    while k <= hi:
        if left[i] < right[j]:
            num[k] = left[i]
            i += 1
        else:
            num[k] = right[j]
            j += 1
        k += 1


def MergeSort(num, lo, hi):
    if lo < hi:
        mid = (lo + hi) / 2
        MergeSort(num, lo, mid)
        MergeSort(num, mid + 1, hi)
        Merge(num, lo, mid, hi)

if __name__ == "__main__":
    n = 1000000
    num = []
    number = []
    for i in range(n):
        num.append(random.randint(0, 100 * n))
        number.append(num[i])

    start = time.clock()
    HeapSort(num)
    end = time.clock()
    # print num
    print end - start

    start = time.clock()
    QuickSort(number, 0, n - 1)
    end = time.clock()
    print end - start
    for i in range(n - 1):
        if num[i] > num[i + 1]:
            print "wrong", i
