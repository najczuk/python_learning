import numpy as np

# some fun with ndarray attributes

b = np.arange(24).reshape(2,12)
print("In: b")
print(b)

print("In: b.ndim")
print(b.ndim)

print("In: b.size")
print(b.size)

print("In: b.itemsize")
print(b.itemsize)

print("In: b.nbytes")
print(b.nbytes)

print("In: b transposed -> b.T")
print(b.T)
