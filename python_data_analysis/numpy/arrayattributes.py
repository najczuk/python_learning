#!/user/bin/env/python
from __future__ import print_function
from numpy import *

# two dimensional array
m = array([arange(2), arange(2)])
print('m array', '\n', m)
print('m shape', '\n', m.shape)

#indexing
m = array([[1, 2], [3, 4]])
print('m array', '\n', m)
print('m[0,0]', '\n', m[0,0])
print('m[0,1]', '\n', m[0,1])
print('m[1,0]', '\n', m[1,0])
print('m[1,1]', '\n', m[1,1])

#slicing
a = arange(9)
print('a[3:7]','\n', a[3:7])
#increment slicing
print('a[0:7:2]','\n', a[0:7:2])
#backwards slicing
print('a[::-1]','\n', a[::-1])



