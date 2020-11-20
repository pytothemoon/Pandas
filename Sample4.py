import pandas as pd 

df=pd.read_csv('data/friend_list_no_head.csv')
print(df)

df=pd.read_csv('data/friend_list_no_head.csv',header=None)
print(df)

df.columns=['name','age','job']

print(df)