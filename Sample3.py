import pandas as pd 

df=pd.read_csv('data/friend_list.txt')
print(df)

df=pd.read_csv('data/friend_list_tab.txt')
print(df)


df=pd.read_csv('data/friend_list_tab.txt',delimiter='\t')
print(df)