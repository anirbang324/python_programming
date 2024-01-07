# x= int(input())
# y= int(input())
# z= int(input())
# def fun1(x,y): #x=11 , y= 14
#     if x > y:
#         return x
#     return y
# def fun2( x, y, z ):
#     return fun1( x, fun1( y, z ))
# print(fun2(x,y,z))

a = int(input("Enter three numbers to find their average"))
b = int(input("Enter another number"))
c = int(input("Enter another number"))
def avg(a,b,c):
    d = a+b+c/3
    return d
print(int(avg(a,b,c)))
