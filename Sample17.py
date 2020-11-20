import pandas as pd

date_list=[
    {
        'yyyy-mm-dd':'2000-06-27'
    },
    {
        'yyyy-mm-dd':'2007-10-27'
    }
]

df=pd.DataFrame(date_list,columns=['yyyy-mm-dd'])

print(df)

def extract_year(row):
    return row.split('-')[0]

df['year']=df['yyyy-mm-dd'].apply(extract_year)
print(df)

friend_dict_list= [
    {'name':'John','midterm':95 , 'final':85},
    {'name':'Ben','midterm':85 , 'final':80},
    {'name':'Jenny','midterm':30 , 'final':10}
]
df= pd.DataFrame(friend_dict_list,columns=['name','midterm','final'])
print(df.head())


df2=pd.DataFrame([['Ben',50,50]],columns=['name','midterm','final'])
print(df2)

df.append(df2,ignore_index=True)
print(df)