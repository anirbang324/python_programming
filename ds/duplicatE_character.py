from collections import Counter
def c1(a):
    b = Counter(a)
    j = -1
    for i in b.values():
        j= j+i
        if(i>1):
            print (b.keys(),[j])
a = input("enter the string:")
c1(a)