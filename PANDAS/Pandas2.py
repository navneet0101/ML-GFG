'''
import pandas as pd
import numpy as np
import time
data=pd.read_csv('train.csv')
'''
'''
print(data.describe())#this ll return all detail like (mean max min std etc)of my dataset.....
print(data.head)#this ll return top 5 colomn
print(data.tail) #this ll return bottom 5 records
print(data.describe(include='all'))#it 'll return unique of them too......
t('%.10f'%(time.time()-start))
'''

'''
#print(['Name'][data['Age'].isna()])#isna returning whre exaclty my missing value ....
#print(data['Age'].mean())#this ll return mean of particular colomn ..,,by deafault inplace is false..

print(data['Age'].fillna(data['Age'].mean(),inplace=True))#it ll contain the value that we want replace 
print(data.describe())
#print(len(data['Name'][data['Age'].isna()]))

#print(len(data['Name'][data['Embarked'].isna()]))
#alternating creating function to findout missing value nd replace it..., if nan repl by mean or by mode
#for numerical --mean
#nt num --mode
'''
'''
import pandas as pd
import numpy as np
import time

data=pd.read_csv('train.csv')
print(data.loc[[1,2,3],['Name','Age','Sex']])

print(data.iloc[10,2])#it ll return that position item,,,,,
print(data.iloc[10:21,1:5])



di={'Name':['raushan','vddfv','sdsfvds','vsvds'],'class':[1,2,3,4],'location':['ds','dfdsf','dsffds','dsffds']}
 
sfd=pd.DataFrame(di)

sfd.tocsv('student.csv')# for saving data in a file...
print(sfd)
'''
'''
gf=data.groupby(['SibSp','Parch'])#this is called EDA
print(gf.sum())
import matplotlib.pyplot as plt

# we have to find the record which is follow some condition......
print(data['Survived'][data['Age']>60] ==1)#??????????? #to find the surviving passengers 

dg=data.groupby(data['Age']>43)#another method#?????
print(dg)
print(plt.show())#???????????  # tablu software....
'''
'''
#see these package for NLP
gtts
speech recog.
pywin
'''









