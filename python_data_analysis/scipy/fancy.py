import scipy.misc
import matplotlib.pyplot as plt
from numpy import *

face = scipy.misc.face()
xmax = face.shape[0]
ymax = face.shape[1]


# face[range(xmax), range(ymax)] = zeros(3,dtype=uint8)
# face[range(xmax-1, -1, -1), range(ymax)] = zeros(3,dtype=uint8)

plt.imshow(face)
plt.show()
