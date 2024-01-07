# Python program to display the Fibonacci sequence
#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.This means to say the nth term is the sum of (n-1)th and (n-2)th term.

def recursionfibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursionfibonacci(n-1) + recursionfibonacci(n-2))

number= int(input("Please enter the range: "))

# check if the number of terms is valid
if number <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(number):
       print(recursionfibonacci(i))