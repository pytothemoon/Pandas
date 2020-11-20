import pandas as pd

friends= [
    {'age':15 , 'job':'student'},
    {'age':25 , 'job':'developer'},
    {'age':30 , 'job':'teacher'}
]

df=pd.DataFrame(friends,index=['John','Jenny','Nate'],
columns=['age','job'])

print(df)

print(df.drop(['John','Nate']))

print(df.drop(['John','Nate'],inplace=True))


friends= [
    {'name':'John','age':15 , 'job':'student'},
    {'name':'Ben','age':25 , 'job':'developer'},
    {'name':'Jenny','age':30 , 'job':'teacher'}
]

df= pd.DataFrame(friends,columns=['name','age','job'])
df=df.drop(df.index[[0,2]])
print(df)