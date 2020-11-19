import pandas as pd 

data_frame=pd.read_csv('data/friend_list.csv')
print(data_frame)
print(data_frame.head(2))
print(data_frame.tail(2))
print(type(data_frame.job))