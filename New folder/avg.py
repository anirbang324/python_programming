num1 = float(input('first number: '))
num2 = float(input('second number:'))
num3 = float(input('third number: '))
def average(num1, num2, num3):
    average = int((num1 + num2 + num3)/3)
    return average
average = average(num1, num2, num3)
print('average = ',average)