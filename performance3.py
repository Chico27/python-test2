import time

resultList = []
for j in range(100):
    start = time.time()
    for i in range(100000000):
        flag = True
    print(str(j+1) + ' times.')
    process_time = time.time() - start
    resultList.append(process_time)
    print(process_time)
    print("")

ave = sum(resultList) / len(resultList)

print('平均: ' + str(ave))
