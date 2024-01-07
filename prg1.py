str1 = "listen"
lst1 = []

for i in str1:
    lst1.append(i)

lst1.sort()

str2 = "silent"

lst2 = []
for i in str2:
    lst2.append(i)
lst2.sort()

# flag = False
# for i in str1:
#     for j in str2:
#         if(i==j):
#             flag = True
# print(flag)

print(lst1)
if lst1==lst2:
    print("yes")
else:
    print("no")


