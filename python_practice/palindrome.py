def pal(string):
    rev_string=string[::1]
    status=1
    if(string!=rev_string):
        status=0
    return status

string=input("Enter the string:")
status=pal(string)
if(status):
    print("It is palindrome")
else:
    print("not palindrome")