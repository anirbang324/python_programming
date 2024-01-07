class A:
    def __init__(self,name1,rolln1,subject1): #constructor
        self.name = name1
        self.rolln = rolln1
        self.subject = subject1
    def details(self):
        print("Name:",self.name)
        print("RollN:",self.rolln)
        print("Subject:",self.subject)
Aryan = A("Aryan",21,"Geometry")
# Aryan.name = "Anirban" #whenever we are running Anirban it is fetching the whole method which is 'details'
# Aryan.rolln = "12000" #we are accessing this object 'Anirban' with self
# Aryan.subject= "geometry"
Aryan.details()