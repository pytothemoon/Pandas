import pandas as pd
friends= [
    {'name':'John','age':15 , 'job':'student'},
    {'name':'Ben','age':25 , 'job':'developer'},
    {'name':'Jenny','age':30 , 'job':'teacher'}
]

df= pd.DataFrame(friends,columns=['name','age','job'])
print(df)
df['salary']=0
print(df)

import numpy as np
df['salary']=np.where(df['job'] !='student','yes','no')

print(df)