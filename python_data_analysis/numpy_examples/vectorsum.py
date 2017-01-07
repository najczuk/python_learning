import sys
from datetime import datetime
import numpy as np


def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n,dtype=numpy.int64) ** 3
    c = a + b
    print(b)
    return c


def pythonsum(n):
    a = []
    b = []
    c = []

    for i in range(n):
        a.append(i ** 2)
        b.append(i ** 3)

        c.append(a[i] + b[i])
    return c


size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("the last 2 elements of the sum", c[-2:])
print("python sum took", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("the last 2 elements of the sum", c[-2:])
print("python sum took", delta.microseconds)
