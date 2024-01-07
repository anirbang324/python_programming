class A:
    def p1(self):
        print("Hello")
class B:
    def p2(self):
        print("Python")
class c(A,B):
    pass

ob1 = c()
ob1.p1()
ob1.p2()

