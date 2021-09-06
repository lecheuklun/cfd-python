
# mwahahaha it begins

import numpy
from matplotlib import pyplot

myarray = numpy.linspace(0, 5, 10) # same as matlab
print(myarray)

d = [5, 'five', 5.0]
for i in d:
    print(type(i))

for i in range(5):
    print('Hi\n')

# slicing arrays

myvals = numpy.array([1,2,3,4,5])
print(myvals)
# print(myvals[5]) # out of range, python 0 indexed (noobs)
print(myvals[0:3])

# assigning

a = numpy.linspace(1,5,5) # 1,2,3,4,5
b = a # same

a[2]=17 # 1,2,17,4,5
print(b) # PRINTS SAME THING AS a !?!??!?!?!
# this is an 'assignment by reference', everything is linked

# editable copy -> use copy
c = a.copy()
a[2] = 3
print(a)
print(c)

numpy.arange(5) # array([0,1,2,3,4])
aa = [x+y for x,y in zip(a,a)]
print(aa)

