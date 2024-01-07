list = [1,2,3,4,5]
n = 2


newlist = []

for i in range(len(list)-n,len(list)):
    newlist.append(list[i])



for i in range(0,len(list)-n):
    newlist.append(list[i])

print(newlist)

