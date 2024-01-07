s = input("enter the string")
b = list(s)
print(b)
c = input("enter the value")
for i in b:
    if(i==c):
        b.remove(c)
v = str(b)


