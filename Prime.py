num = 1000
result = []
i = 0
while i < num:
    result += [True]
    i += 1

for i in range(2, num):
    if result[i]:
        print i
        j = 2
        while i * j < num:
            result[i * j] = False
            j = j + 1
