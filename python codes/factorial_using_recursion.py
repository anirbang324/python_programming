def fact(n):
    if(n==0):
        return 1 #factorial of 0 is 1
    return n*fact(n-1)
n = int(input("enter the value:"))
result = fact(n)
print(result)