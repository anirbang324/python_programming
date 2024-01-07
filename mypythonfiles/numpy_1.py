import numpy
from numpy.core.shape_base import stack
a = numpy.array([2,3,4,5,6])
b = numpy.array([5,7,8,9,1])
d = numpy.array([50,20,30,10,40])

# c = numpy.hstack((a,b,d),axis=1)
# s = numpy.dstack((a,b,d),axis=1)
x = numpy.vstack((a,b,d),axis=1)

# print(c)
print(s)
print(x)
# print(b.base)