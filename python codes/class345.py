class Person:
    def A(self):
           Name=input(("Enter Your Name:"))
           Age=input(("Enter Your Age:"))
           print(Name,Age)

class d(Person):
    def B(self):
        Class=input("Enter Your Class:")
        print(Class)

ob1 = d()
ob1.A()
ob1.B()