class A:
    def p4(self):
        print("Hello,this is parent")
class B(A):
    def p4(self):
        print("Hello,this is child")

ob1 = B()
ob1.p4()