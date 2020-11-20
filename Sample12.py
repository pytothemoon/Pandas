import pandas as pd

df=pd.read_csv('data/friend_list_no_head.csv',header=None,names=['name','age','job'])

print(df)

df_filtered = df[['name','age']]
print(df_filtered)

print(df.filter(items=['age','job']))


print(df.filter(like='a',axis=1))

print(df.filter(regex='e$',axis=1))