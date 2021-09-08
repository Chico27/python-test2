import time
from collections import defaultdict

breakfast = ['kome', 'pan', 'kome', 'kome', 'cereal', 'pan', 'kome']

resultList = []
for j in range(100):
    start = time.time()
    for i in range(100000):
        numbers = defaultdict(lambda: 0)
        for b in breakfast:
            numbers[b] += 1
    process_time = time.time() - start
    print(str(j+1) + ' times.')
    resultList.append(process_time)
    print(process_time)
    print('')

ave = sum(resultList) / len(resultList)

print(resultList)
print('平均: ' + str(ave))
