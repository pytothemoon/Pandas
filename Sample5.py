import pandas as pd 

df=pd.read_csv('data/friend_list_no_head.csv',header=None,names=['name','age','job'])
print(df)