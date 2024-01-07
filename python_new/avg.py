# Write a Python function to find the Max of three numbers.

def fun(n1,n2,n3):
    if (n1 > n2 and n1 > n3):
        print("n1 is largest")
    elif (n2 > n1 and n2 >n3):
        print("n2 is largest")
    elif(n3 > n1 and n3 >n2):
        print("n3 is largest")
fun(12,13,14)
