import time

resultList = []
for j in range(10):
    testList = []
    start = time.time()
    for i in range(1000000):
        print('this is', 'test')
    process_time = time.time() - start
    print(str(j+1) + ' times.')
    resultList.append(process_time)

ave = sum(resultList) / len(resultList)

print(resultList)
print('平均: ' + str(ave))
