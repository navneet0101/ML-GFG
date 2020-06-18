
import numpy as np
#for array slicing 
'''a=np.array([[1,2,4],[3,3,4],[4,5,6]])
print(a)
print(a[0:,1:])

#for Stacking.......
a=np.arange(1,7).reshape((2,3))
b=np.arange(7,13).reshape((2,3))
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(a)
'''
a=np.arange(1,7).reshape((2,3))
b=np.arange(7,13).reshape((2,3))

r=np.hsplit(a,3)
for i in range(0,3):
    print(r[i])
print(a.ndim)

r2=np.vsplit(b,2)
for i in range(0,2):
    print(r2[i])
print(b.ndim)
print(b)

