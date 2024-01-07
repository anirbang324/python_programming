def dec(f):
    def fun2(a):
        return[f(val[0],val[1]) for val in a]
    return fun2()

@dec
def fun1(c,b):
    return c*b
print(fun1([(6,7),(4,5),(6,8),(1,5)]))