v = input()
c = reversed(v)  # reversing the string

if list(v)==list(c):
    print(v,"is palindrome")
else:
    print(v,"is not palindrome")