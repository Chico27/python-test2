import time

resultList = []
for j in range(100):
    root_list = [24, 24, 24, 24]
    append_list1 = [12] * 10
    append_list2 = [24] * 2
    append_list3 = [24] * 5
    start = time.time()
    for i in range(100000):
        root_list += append_list1
        root_list += append_list2
        root_list += append_list3
    process_time = time.time() - start
    print(str(j+1) + ' times.')
    resultList.append(process_time)
    print(process_time)
    print('')

ave = sum(resultList) / len(resultList)

print(resultList)
print('平均: ' + str(ave))
