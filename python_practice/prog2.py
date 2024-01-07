num = int(input())
a = num
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
new = int(reversed_num)
print(a)
print(new)


# Python program to
# compute sum of digits in
# number.

# Function to get sum of digits

sum = 0
for digit in str(num):
    sum += int(digit)
val = sum


for i in range(val):
    print(new)
    new= new+1

