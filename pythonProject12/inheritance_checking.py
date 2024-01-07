class a:
    pass
class b(a):
    pass

# print(issubclass(b,a))
# print(issubclass(a,b))

ob1 = b()
ob2 = a()

print(isinstance(ob1,a))

print(isinstance(ob2,b))