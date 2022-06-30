import pandas as pd
import numpy as np
#create  a series with random number
s = pd.Series(np.random.randn(4))
print("Is the Object empty")
print(s.empty)
#s = pd.Series()
#print(s.empty)
 #return the number of dimensions of the object. By definition a series is a 1D data structure
print(s)
print("The dimension of the object:")
print(s.ndim)




#create a Dictonary of series raw format
d = {'Name':pd.Series(['Tom','James','Ricky','purna','sita']),'Age':pd.Series([24,25,45,45,12]),'Rating':pd.Series([42.2,45,2.1,356.23,78.12])}

#crate a dataframe
df = pd.DataFrame(d)
print("Our data series is:")
print(df)
#transpose of the above series dictionary column format
print(df.T)
print(df.shape) #it represent the number of row and column
print(df.size)#it represent the total calculation fo row and column shape
print(df.head(4))# it reprsent the show the data in total record from the top
print(df.tail(2))# it shorting the and show the data in total record
#sum
print(df.sum())#sum the series
print(df.sum(1))#sum the special series
print(df.mean())#means the series
print(df.describe())#describe the series

print(df.min())#count the minumum values
print(df.max())#count the maxmum values
print(df.describe(include='all'))
print(df.sort_index(ascending=False))#desending order sorting
print(df.sort_index(ascending=False, axis=1))#ascending by rating
print(df.sort_values(by='Name',ascending=True))# acsending by first order "name"
