import pandas as pd 

s1= pd.core.series.Series([1,2,3])
s2= pd.core.series.Series(['one','two','three'])
print(pd.DataFrame(data=dict(num=s1,word=s2)))

