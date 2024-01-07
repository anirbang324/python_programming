#1.write a python function to find the max of three numbers.
x= int(input())
y= int(input())
z= int(input())
def fun1(x,y): #x=11 , y= 14
    if x > y:
        return x
    return y
def fun2( x, y, z ):
    return fun1( x, fun1( y, z ))
print(fun2(x,y,z))

# # #2.Write a Python function to sum all the numbers in a list.
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
#
# print(sum((8, 2, 3, 0, 7)))
#
# # #3.Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def list1(l):
#   num = []
#   for a in l:
#     if a not in num:
#       num.append(a)
#   return num
# print('unique elements are')
# print(list1([1,2,4,5,4,5,6,9,10]))
# #
# # #4.Write a Python function that takes a number as a parameter and check the number is prime or not.
# # def prime(a):
# #     for i in range (2,a) :
# #         if a % i == 0 :
# #             print("number is prime")
# #         else:
# #             print("number is not prime")
# # a = int(input("Enter a number : "))
# # prime(a)
# #
# #
# #
# # #5.Write a Python function that checks whether a passed string is palindrome or not.
# # def pal(a):
# #
# #     if (a == a[::-1]):
#         print("The string is a palindrome")
#     else:
#         print("The string is not a palindrome")
#
# a = input("Enter string:")
# pal(a)