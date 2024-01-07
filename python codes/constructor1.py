class A:
    def __init__(self,name1,salary1,role1): #constructor
        self.name = name1
        self.salary = salary1
        self.role = role1
    def details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Role:",self.role)

ob1 = A("Anirban",12000,"Tutor")
# ob1 = A(name,salary,role)
# ob1.name = "Anirban" #whenever we are running Anirban it is fetching the whole method which is 'details'
# ob1.salary = "12000" #we are accessing this object 'Anirban' with self
# ob1.role = "Tutor"
ob1.details()