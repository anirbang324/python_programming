def fun(integers):
    for i in integers:
        print(i)
numbers = []
num = int(input("enter the number of elements in  the list: "))
for i in range(0,num):
    element = input()
    numbers.append(element)
fun(numbers)