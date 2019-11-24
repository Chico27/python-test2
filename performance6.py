import time

test = 'aaa'
resultList = []
for j in range(100):
    start = time.time()
    for i in range(100000000):
        if not test == 'bbb':
            pass
    print(str(j+1) + ' times.')
    process_time = time.time() - start
    resultList.append(process_time)
    print(process_time)
    print('')

ave = sum(resultList) / len(resultList)

print(resultList)
print('平均: ' + str(ave))
