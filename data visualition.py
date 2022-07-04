import pandas as pd # pd is a nick name
import numpy as np
import matplotlib.pyplot as plot #for scattor chart call
dataframe = pd.read_csv('scottish_hills.csv')
#print(dataframe)
#a = pd.read_excel('excel.xlsx')
#print(a)
print(dataframe['Hill Name'])
print(dataframe['Height'])
print(dataframe.iloc[5])# Give you the row at position five.
print(dataframe.iloc[0,3])#first row and 3 column
print(dataframe.loc[:, ['Hill Name','Height','Latitude']])# getting all records with specified column
print(dataframe.loc[[1,10], :]) #Row 1 and 10 reocrd wiht all (column(:))
print(dataframe.loc[(dataframe['Height']>500)& (dataframe['Hill Name']=='An Socach')])# Height >500 data Hill Name An socach only


dd = (dataframe.loc[(dataframe['Height']>100)& (dataframe['Hill Name']=='An Socach')])
print(dd.loc[:,['Hill Name','Height','Latitude']])#

#for scatter chart
x = dataframe.Height
y = dataframe.Latitude
plot.scatter(x, y)
plot.show()

