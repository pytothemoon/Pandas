import pandas as pd
friend_dict_list= [
    {'name':'John','midterm':95 , 'final':85},
    {'name':'Ben','midterm':85 , 'final':80},
    {'name':'Jenny','midterm':30 , 'final':10}
]

df= pd.DataFrame(friend_dict_list,columns=['name','midterm','final'])
print(df.head())
df['total']=df['midterm']+df['final']
print(df)

df['average']=df['total']/2
print(df)


grades=[]

for row in df['average']:
    if row >=90:
        grades.append('A')
    elif  row >=80:
        grades.append('B')
    else :
        grades.append('F')
df['grade']=grades
print(df)


def pass_or_fail(row):
    if row !='F':
        return "Pass"
    else :
        return "Fail"

df.grade=df.grade.apply(pass_or_fail)
print(df)