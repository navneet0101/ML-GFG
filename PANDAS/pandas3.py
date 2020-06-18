'''
import pandas as pd
import numpy as np
import time
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   #c drawing the plot and graph..


data=pd.read_csv('train.csv')
#print(data.loc[[1,2,3],['Name','Age','Sex']])

fig=plt.figure(figsize=(100,100))

fig.add_subplot(3,3,1)
sns.countplot(x='Pclass',hue='Survived',data=data) 
plt.show()

fig.add_subplot(3,3,2)
sns.countplot(x='Sex',data=data)
plt.show()

fig.add_subplot(3,3,3)
sns.countplot(x='Age',data=data)
plt.show()

sns.distplot(data['Age'].dropna())
plt.show()

sns.swarmplot(data['Age'],data['Fare'],hue=data['Sex'])
plt.show()
#training data and test data attribute should be same...



