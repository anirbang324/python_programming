# cook your dish here
n = int(input())
lst = []
lsta = []
lstb = []
for i in range(n):
    a,b = map(int,input().split())
    c = int(a-b)
    lst.append(c)
    lsta.append(a)
    lstb.append(b)
maxa = max(lsta)
maxb = max(lstb)
maxnum = max(lst)

if maxa>maxb:
    print(1," ",maxnum)
else:
    print(2," ",maxnum)