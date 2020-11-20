import pandas as pd


friend_list =[
['John',20,'student'],
['Nate',30,'teacher']
]

column_name=['name','age','job']

df=pd.DataFrame.from_records(friend_list,columns=column_name)
print(df.head)