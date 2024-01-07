s=1
try:
    print(s)
except NameError:
    print("s is undefined")
else:
    print("Exception has not occured")
finally:
    print("operation succesfull")