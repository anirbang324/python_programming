n = int(input())
str1 = ''
lst = []
for i in range(n):
    lst.append(i)

for j in range(1, len(lst) + 1):
    j1 = str(j)
    str1 = str1 + j1

print(str1)
