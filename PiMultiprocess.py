import multiprocessing
import os
import time
import random
import math


def worker(num, l, t):
    """thread worker function"""
    print 'Worker:', num

    result_in = 0
    j = 0
    while j < t:
        j = j + 1
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        if math.sqrt(x * x + y * y) <= 10:
            result_in = result_in + 1
        if j % 1e7 == 0:
            print 'Worker:', num, '  ', j/1e7
    l.append(result_in)
    # print 'Worker:', ' qsize ', queue.qsize()
    return


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    lt = manager.list()
    total = int(5e7)
    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(worker, (i, lt, total, ))
    pool.close()
    pool.join()
    final = 0
    print lt
    for i in lt:
        final = final + i
    print float(final) / total / 5 * 4


# def fun1(a, q):
#     q.put(a)
#
# if __name__ == '__main__':
#     manager = multiprocessing.Manager()
#     q = manager.Queue()
#     p = multiprocessing.Pool()
#     x = [a for a in range(1,5)]
#     print(x)
#     while True:
#         for each in x:
#             p.apply_async(fun1, (each, q))
#         # p.close()
#         # p.join()
#         for i in range(q.qsize()):
#             print(q.get())
#         time.sleep(3)
