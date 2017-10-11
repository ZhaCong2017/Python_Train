import random
import math

total = int(1e9)
divisor = int(1e7)
result_in = 0

i = 0
while i < total:
    i = i + 1
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    if x * x + y * y <= 100:
        result_in = result_in + 1
    if i % divisor == 0:
        print str(i / divisor) + '% done'
print float(result_in) / total * 4
