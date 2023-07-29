import psutil
x = list(psutil.process_iter())

for i in range(len(x)):
     s = x[i].name()
     print(s)

