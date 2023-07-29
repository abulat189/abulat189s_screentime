import psutil
import time

while 1:
    x = list(psutil.process_iter())
    for i in range(len(x)):
        process = x[i]
        running = time.time() - x[i].create_time()
        print(process.name(), running)
    time.sleep(10)




