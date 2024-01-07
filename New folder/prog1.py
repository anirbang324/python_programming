lst = [4,3,5,1,4,4]
lst2 = []
sorted(lst)
c = 0
val = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        val = lst[i]-lst[j]
    lst2.append(val)
a = lst2[0]
# print(a)
for i in lst2:
    if lst2[i] == a:
        c =c+1
print(c-1)
