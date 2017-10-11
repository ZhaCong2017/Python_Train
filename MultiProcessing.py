import multiprocessing
import time


def worker(num):
    print 'worker', num, ' start'
    time.sleep(2)
    print 'worker', num, ' end'


def work1(num, q):
    print 'worker', num, ' start'
    q.put(num)
    time.sleep(1)
    print 'worker', num, ' end'


def work2(num, q):
    q.get(num)
    print 'worker', num, ' start'
    time.sleep(1)
    print 'worker', num, ' end'

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    pool = multiprocessing.Pool(3)
    for i in range(15):
        pool.apply_async(worker, (i,))
    pool.close()
    pool.join()
    print "main end"
