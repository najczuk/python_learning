from numpy import *

# more array attributes

print("In: b = arange(24).reshape(2,12)")
b = arange(24).reshape(2,12)
print(b)

print("In: b.ndim")
print(b.ndim)

print("In: b.size")
print(b.size)

f = b.flat
print("In: for item in f: print item")
for item in f:
    print(item)
