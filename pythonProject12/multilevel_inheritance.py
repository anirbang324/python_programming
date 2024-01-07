class A:
    def p1(self):
        print("Hello")
class B(A):
    def p2(self):
        print("Python")
class c(B):
    pass

ob1 = c()
ob1.p1()
ob1.p2()
