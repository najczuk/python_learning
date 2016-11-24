from numpy import *

# array definitions
print("In: a = arange(9).reshape(3,3)")
a = arange(9).reshape(3,3)
print(a)

print("In: b = 2 * a")
b = 2 * a
print(b)

# horizontal stacking
print("In: hstack((a,b))  OR concatenate((a,b), axis = 1)")
print(hstack((a,b)))
print(concatenate((a,b), axis = 1))


# vertical stacking
print("In: vstack((a,b))  OR concatenate((a,b), axis = 0)")
print(vstack((a,b)))
print(concatenate((a,b), axis = 0))

# depth stacking
print("In: dstack((a,b))")
print(dstack((a,b)))


# column stacking column_stack((a,b)) == hstack((a,b) == concatenate((a,b),axis=0))
print("In: oned = arange(2), twice_oned = oned * 2")
oned = arange(2)
print(oned)
twice_oned = oned * 2
print(twice_oned)
print("In: column_stack(oned,twice_oned)")
print(column_stack((oned,twice_oned)))

# the same with row_stack((a,b)) == vstack((a,b) == concatenate((a,b),axis=1))


