import pandas as pd
import numpy as np
import time
data=pd.read_csv('train.csv')

'''
print(data.describe())#this ll return all detail like (mean max min std etc)of my dataset.....
print(data.head)#this ll return top 5 colomn
print(data.tail) #this ll return bottom 5 records
print(data.describe(include='all'))#it 'll return unique of them too......
'''

'''
b=data
z=[]
#another way of fetching dataset...... 
for x in range(0,10):
    b=data['Name'][x]
    a=b.split(',')[1].split()   #????????????       
    z.append(a[0])
print(z)
'''

'''
#checking time taken while using for vs dataframe........dataframe takes less time..
start=time.time()
print('%.10f'%(time.time()-start)) #gives time of cpu #ctime() isfor clock time...

data['title']=data['Name'].apply (lambda x:x.split(',')[1].split())#lmbda is use to defining one line function
print('%.10f'%(time.time()-start))
'''


#print(['Name'][data['Age'].isna()])#isna returning whre exaclty my missing value ....
#print(data['Age'].mean())#this ll return mean of particular colomn ..,,by deafault inplace is false..

print(data['Age'].fillna(data['Age'].mean(),inplace=True))#it ll contain the value that we want replace 

#print(len(data['Name'][data['Age'].isna()]))

#print(len(data['Name'][data['Embarked'].isna()]))
#alternating creating function to findout missing value nd replace it..., if nan repl by mean or by mode
#for numerical --mean
#nt num --mode

