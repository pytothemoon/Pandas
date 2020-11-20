import pandas as pd
friends= [
    {'name':'John','age':15 , 'job':'student'},
    {'name':'Ben','age':25 , 'job':'developer'},
    {'name':'Jenny','age':30 , 'job':'teacher'}
]

df= pd.DataFrame(friends,columns=['name','age','job'])
print(df[df.age>20])

df=df.drop('age',axis=1)
print(df)