import random


def binarysearch(num, lo, hi, target):
    if lo >= hi and num[lo] != target:
        return -1
    mid = lo + (hi - lo) / 2
    if num[mid] == target:
        return mid
    elif num[mid] < target:
        return binarysearch(num, mid + 1, hi, target)
    else:
        return binarysearch(num, lo, mid - 1, target)


def main():
    lst = []
    for i in range(15):
        lst.append(i * 2)
    print binarysearch(lst, 0, 14, 30)


if __name__ == '__main__':
    main()
