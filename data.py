import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({'Name':['purna','purna','purna',
                           'manisha','manisha','manisha','manisha',
                           'mina','mina'],
                   'votes':[12,12,30,
                            23,42,25,26,
                            20,20]})
df.groupby(['Name']).sum().plot(kind='pie',autopct='%1.0f%%',y='votes',startangle=98)
df.plot()
