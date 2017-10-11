import random
import time


def findk(num, lo, hi, k):
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
        if i - lo + 1 == k:
            return
        elif i - lo + 1 < k:
            findk(num, i + 1, hi, k - i + lo - 1)
        else:
            findk(num, lo, i - 1, k)


if __name__ == '__main__':
    n = int(1e5)
    k = 1000
    num = []
    i = 0
    while i < n:
        num.append(random.randint(0, 100 * n))
        i += 1

    print "start"
    start = time.clock()
    findk(num, 0, len(num) - 1, n - k)
    end = time.clock()
    print end - start, 's'
    # print num
    tim = 0

    start = time.clock()
    for i in range(k):
        for j in range(n - k):
            if num[n - i - 1] < num[j]:
                print tim
                tim += 1
        if i % 1000 == 0:
            print i, "done!"
    end = time.clock()
    print end - start, 's'


