import random
import numpy
import datetime

start = datetime.datetime(2018,1,15,23,34,59)

p = numpy.ones((300,))
p[-1] = 0

for i in range(2000):
    e = random.choice(p)
    if e == 0:
        start += datetime.timedelta(0,10)

        k = random.choice(['1','2','3'])
        print(i+1, start, 'UVES', '\t\t Error %s: something ununderstandable'%k)
    
    else:
        start += datetime.timedelta(0,10)
        print(i+1, start, 'UVES', '\t\t No Problem! all is fine!')
