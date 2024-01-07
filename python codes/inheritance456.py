class A: #1st
    def fun1(self):
        print("Hello World")

class B(A):   #levelwise  #2nd
    def fun2(self):
        print("A")
class C(B): #3rd
    def fun3(self):
        print("B")

class D(C): #4th
    pass

ob1 = D()
ob1.fun1()
ob1.fun2()
ob1.fun3()
