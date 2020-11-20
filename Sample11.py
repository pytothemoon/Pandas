import pandas as pd

friend_list=[
    ['John',20,'student'],
    ['Jenny',30,'developer'],
    ['Nate',30,'teacher']
]

df=pd.DataFrame.from_records(friend_list)

print(df)

print(df.iloc[:,0:2])
