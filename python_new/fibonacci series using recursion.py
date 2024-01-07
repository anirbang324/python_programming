# 1st Fibonacci number = 0 (by assumption)
# 2nd Fibonacci number = 1 (by assumption)
# 3rd Fibonacci number = 1st + 2nd
# = 0 + 1
# = 1
# 4th Fibonacci number = 2nd + 3rd
# = 1 + 1
# = 2
# 5th Fibonacci number = 3rd + 4th
# = 1 + 2
# = 3
# 6th Fibonacci number = 4th + 5th
# = 2 + 3
# = 5
# So, nth Fibonacci number = (n-1)th Fibonacci + (n-2)th Fibonacci

def Fibonacci(pos):
    # check for the terminating condition
    if pos <= 1:
        # Return the value for position 1, here it is 0
        return 0
    if pos == 2:
        # return the value for position 2, here it is 1
        return 1

    # perform some operation with the arguments
    # Calculate the (n-1)th number by calling the function itself
    n_1 = Fibonacci(pos - 1)

    # calculation  the (n-2)th number by calling the function itself again
    n_2 = Fibonacci(pos - 2)

    # calculate the fibo number
    n = n_1 + n_2

    # return the fibo number
    return n

a = int(input())
nth_fibo = Fibonacci(a)

print(nth_fibo)