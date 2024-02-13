import time

resultList = []
for j in range(100):
    testList = []
    start = time.time()
    for i in range(10000000):
        a = 1 - 1
    process_time = time.time() - start
    print(str(j+1) + ' times.')
    resultList.append(process_time)
    print(process_time)
    print('')

ave = sum(resultList) / len(resultList)

print(resultList)
print('平均: ' + str(ave))
