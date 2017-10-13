def perm(low, high, num):
    global n
    if low >= high:
        n += 1
        # print num
        return
    i = low
    while i <= high:
        num[low], num[i] = num[i], num[low]
        perm(low + 1, high, num)
        num[low], num[i] = num[i], num[low]
        i += 1


if __name__ == '__main__':
    i = 1
    while i <= 10:
        n = 0
        num = range(1, i + 1)
        perm(0, i - 1, num)
        total = 1
        tmp = i
        while tmp >= 2:
            total *= tmp
            tmp -= 1
        if total == n:
            print n, " True"
        else:
            print "False"
        if i % 5 == 0:
            print i, ' done!'
        i += 1
