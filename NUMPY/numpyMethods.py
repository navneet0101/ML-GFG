import numpy as np

list1=[[1,2,3.0,6],[434,4234,4243,3432],[4324,424,432,4]]

array1=np.array(list1)
print(type(array1))#return type of array
print(array1)

print(array1.dtype)
print(array1.itemsize)
print(np.shape(array1))#print dimension of array
print(array1.shape)#print dimension of array

array4 = array1.reshape(6,2)


a=np.array([[1,2,3],[2,3,4],[3,4,5]],dtype=np.float64)
print(a)

array2=np.arange(1,10,2)#creating array from ranging values
print(array2)
'''
print(array2.ndim)

array3=array2.reshape(2,2,2)
print(array3)
print(array3.ndim)

array5=np.linspace(1,20,20)

print(array5)






print(a.shape())
print(l.ndim)

#l=l.reshape((2,5))

a=np.arange(5,15,1.7)

print(a)'''

