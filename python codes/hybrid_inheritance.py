class A:
    def fun1(self):
        print("Hey there, you are in class A")
class B(A):
    def fun2(self):
        print("Hey there, you are in class B")
class C(A):
    def fun3(self):
        print("Hey there, you are in class C")
class D(C,A): #line 13
    def fun4(self):
        print("Hey there, you are in the class D")#main program
ref = D()
ref.fun4()
ref.fun3()
ref.fun1()
