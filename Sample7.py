import pandas as pd
from collections import OrderedDict


friend_ordered_dict=OrderedDict(
    [
        ('name',['John','Nate']),
        ('age',[25,30]),
        ('job',['student','teacher'])
    ]
)

df=pd.DataFrame.from_dict(friend_ordered_dict)
df=df[['name','age','job']]

print(df.head)