from numpy import *

#
#demonstrates multi-dimensional arrays slicing
#


# reshape method
print("b = np.arange(24).reshape(2,3,4)")
b = arange(24).reshape(2,3,4)

print("In: b - array of two arrays")
print(b)
print("In: b[0] first array")
print(b[0])

# ravel - flattening array without alocating new memory

print("In: b.ravel()")
print(b.ravel())

# flatten - flattening which creates copy of flattened array
print("In: b.flatten()")
print(b.flatten())


# reshape with touple modification
print("In b.shape = (6,4)")
b.shape = (6,4)
print(b)

# transpose
print("In: b.transpose()")
print(b.transpose())

# resize - works like reshape but changes array in place
print("In b.resize((2,12))")
b.resize((2,12))
print(b)