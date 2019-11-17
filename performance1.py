import time
start = time.time()
a = ''
for i in range(100000000):
   if a == '':
       pass
process_time = time.time() - start
print(process_time)

