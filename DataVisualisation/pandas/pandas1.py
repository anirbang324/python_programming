
#1 : creation of a simple data frame
import numpy as np
import pandas as pd

user1 = pd.DataFrame([1,'Anirban',23,'M','Science'],
                     [2,'Utsav',22,'M','Science'])
# Dataframe by column header
# print(user1)
col = ['Roll No','Name','Age','Gender','Subject']

#another data frame
user2 = pd.DataFrame([[1,'Anirban',23,'M','Science'],
                     [2,'Utsav',22,'M','Science']],
                     columns = col)
# print(user2)
#convertion of data into dataframe from dictionary

user3 = pd.DataFrame(dict(Roll_num = [1,2],
                          Name = ['Anirban','Utsav'],
                          Gender = ['M','M'],
                          Age = [22,23],
                          Subject = ['Science','Science']))
# print(user3)


#making data frame using series

x= [1,2,3,4,5,6]

#creation of series

s = pd.Series(x)
#add index to series
Index = ['a','b','c','d','e','f']
s1 = pd.Series(data = x,index=Index)

df_s = pd.DataFrame(s1)
print(df_s.loc['c'])