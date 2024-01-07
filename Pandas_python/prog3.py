import pandas as pd
data = {
    "list1" : [4,5,6],
    "list2" : [1,2,3]
}
d = pd.DataFrame(data)
print(d.loc[[0,1]])