import pandas as pd


friends=[
    {'name':'Jone','age':20,'job':'student'},
    {'name':'Jenny','age':30,'job':None},  
    {'name':'Nate','age':20,'job':'teacher'}
]

df=pd.DataFrame(friends)
df=df[['name','age','job']]

print(df.head())

df.to_csv('friends.csv',index=False,header=True,na_rep='-')