#!/user/bin/env/python

import sys
from datetime import datetime
import numpy as np

"""
This program demonstrates vector addition the Python way.
Run from the command line as follows
    python vectorsum.py n
where n is an integer that specifies the size of the vectors.

The first vector to be added contains the squares of 0 up to n.
The second vector contains the cubes of 0 up to n.
The program prints the last 2 elements of the sum and the elapsed
time.
"""


def numpysum(n):
    a = np.arange(n, dtype=np.int64) ** 2
    b = np.arange(n, dtype=np.int64) ** 3
    c = a + b
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
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)
