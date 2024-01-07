from scipy.optimize import root   #x+cos(x)
from math import cos
def fun1(x):
    return x+cos(x)
m=root(fun1,0)
print(m.x)
# x^2+x+2

# from scipy.optimize import minimize
# def fun1(x):
#     return x**2+x+2
# m= minimize(fun1,0,method='BFGS')
# print(m)