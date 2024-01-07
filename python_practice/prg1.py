import numpy as np
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
arr1 =[]
arr2 = []
range1 = b+(n-1)*a
range2 = d+(n-1)*c
c1 = 0
c2 = 0
for i in range(b,range1):
    c1= c1+1
    b = b+(a*c1)
    arr1.append(b)

for i in range(d+c,range2):
    c2= c2+1
    d = d+(c*c2)
    arr2.append(d)

n1 = len(arr1)
n2 = len(arr2)


arr1.sort()
arr2.sort()

for i in range(0,n1):
    if(arr1[i]==arr2[i]):
        print(i)
        break
