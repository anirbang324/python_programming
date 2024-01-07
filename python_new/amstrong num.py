number = int(input("enter the number: "))
sum = 0
temp = number

while temp>0:
    i = temp%10
    sum= sum+i**3
    temp=temp//10
if sum == number:
    print(number,"is a amstrong number")
else:
    print(number,"is not a amstrong number")