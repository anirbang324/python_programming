a = int(input("enter the value for a:"))
b = int(input("enter the value for b:"))
c = int(input("enter the value for c:"))
if(a>b and a>c):
    print(a," is largest")
elif(b>a and b>c):
    print(b," is largest")
elif(c>a and c>b):
    print(c," is largest")
else:
    print("please enter the right number")