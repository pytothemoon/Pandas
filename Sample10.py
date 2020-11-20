import pandas as pd


friends=[
    {'name':'Jone','age':20,'job':'student'},
    {'name':'Jenny','age':30,'job':None},  
    {'name':'Nate','age':30,'job':'teacher'}
]
df=pd.DataFrame(friends)
df=df[['name','age','job']]

print(df.head())
print(df[1:3])
print(df.loc[[0,2]])
print(df[df.age>25])
print(df.query('age>25'))
print(df[(df.age>25)&(df.name=='Nate')])
