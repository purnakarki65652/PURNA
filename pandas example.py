import pandas as pd
import numpy as np

#reading from csv files
df = pd.read_csv('phonenumber.csv')
print(df.to_string())

#creating empty series
ser = pd.Series()
print(ser)
#simply array
data = np.array(['g','e','e','k','s'])
ser = pd.Series(data, index=[10,11,12,13,14])# index ramdomly
ser = pd.Series(data) #list o to ....
print(ser)

#creating a series from list
list = ['P','Y','T','H']
ser =pd.Series(list)
print(ser)


#creating a series form dictonary
dict ={
    'Python': 2152,
    'Java': 546665,
    'C#': 465456,
}
ser =pd.Series(dict)
print(ser)

#pandas data frame consist of three principal component the data, the rows and column
df = pd.DataFrame()
print(df)
list = ['P','Y','T','H']
df = pd.DataFrame(list)
print(df)


#data = [['Ram',40],['sita', 39],['Manisha',10]]
#df = pd.DataFrame(data, columns=['Name','Age'])
#print(df)

#salary =[['Ram',400000],['sita',50000],['manisha',100000]]
#df = pd.DataFrame(data, columns=['Name','salary'])
#print(df)

#crating dataframe via dictionery
#data = {'Name':{['Ram','sita','manisha'],'Age':['40','30','28'] ,'salary':[400000,50000,100000]}
#df = pd.DataFrame(data)
#print(df)

