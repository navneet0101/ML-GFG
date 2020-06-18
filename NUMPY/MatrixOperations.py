import numpy as np
import sys
'''a=np.arange(12).reshape((3,4))
print(a)
print(a.itemsize)
print(a.size)
print(a.dtype)
print(a.ravel())
print(a.ndim)
print(a.shape)
print(np.linspace(1,20,5))
print(a.reshape(2,6))
print(np.std(a))
b=np.identity(3)
print(b)
#c=np.arange(215).reshape(())
#d= c>7
d=np.eye(4,k=1)
print(d

a=np.random.randint(1,10,9)
a=a.reshape((3,3))
print(a)
b=np.random.randint(1,10,9)
b=b.reshape((3,3))
print(b)
c=np.matmul(a,b) #it will multiply 
print(c)
print(a*b)


a=np.random.randint(1,10,9)
a=a.reshape((3,3))
a=np.mat(a)
print(a)

b=np.random.randint(1,10,9)
b=b.reshape((3,3))
b=np.mat(b)
print(b)
print(a*b)
c=np.matmul(a,b) #it will multiply 
print(c)
#print(a*b)

np.random.seed(6)


a=np.random.randint(1,10,9)
a=a.reshape((3,3))
print(a)
b=np.random.randint(1,10,9)
b=b.reshape((3,3))
print(b)

#print(np.hsplit(a,3))
#print(np.vsplit(b,3))
v=np.concatenate((a,b),axis=0)
print(v)#row wise concatenation
#print(np.concatenate((a,b),axis=1))#colomn wise con....

a=np.mat(a)#now it becomes matrix we can now perform a*b 
b=np.mat(b)


#print(a*b)

c=a  #it will affect a matric too.,
print(np.may_share_memory(a,c)) #to check both of them are sharing same memory or not(true/,false)
print(a)
c=a.copy() #it will work well
print(c)
c[0][0]=755  #it will affect a matric too.,
print(c)
print(a)

print(a.flatten())#it will convert array in one dimension

mydt=np.dtype([('city',np.unicode,'S34'),('population',np.int),('Area',np.int)])#it will take in same manner type like 1st string 2nd nd 3rd int
a=np.array([('delhi',455,65),('mumbai',344,214),('pune',143,434)],dtype=mydt)

np.savetxt('poplRecord.txt',a,fmt='%.6s,%.6d,%.7d',delimiter=',')
#print(a['city'])
#print(a['population'])
#print(a['Area'])
#b=np.loadtxt('poplRecord.txt',dtype=mydt)

print(a)
b=np.genfromtxt('poplRecord.txt')

print(b)

#titanic dataset have to dwnld
#towardsdatascience
#analitics vidya
#sentdex
#programz
#gg


e=np.arange(9)
f=[1,2,3,43,3,32,4,5,6]
print(sys.getsizeof(5)*len(f))
print(e.itemsize*e.size)
'''
mydt=np.dtype([('First name',np.unicode,'S34'),('Title',np.unicode,'S34'),('last name',np.unicode,'S34')])#it will take in same manner type like 1st string 2nd nd 3rd int
a=np.array([('Raushan','mr','Sharma'),('heena','mrs','Sharma'),('vishal','mr','Sharma')],dtype=mydt)
print(a[0:3][0:3])
