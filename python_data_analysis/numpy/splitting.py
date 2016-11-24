from numpy import *
# splitting splits array into thre parts of the same size and shape
a = array([
    [0,1,2],
    [3,4,5],
    [6,7,8]
])

print("In: a")
print(a)

# horizontal split
print("In: hsplit(a,3) == split(a,3,axis=1)")
print(hsplit(a,3))
print(split(a,3,axis=1))

#vertical split
print("In: vsplit(a,3) == split(a,3,axis=0)")
print(vsplit(a,3))
print(split(a,3,axis=0))

# depth-wise splitting
print("In: c = arange(27).reshape(3, 3, 3)")
c = arange(27).reshape(3, 3, 3)
print(c)

print("In: dsplit(c,3)")
print(dsplit(c,3))