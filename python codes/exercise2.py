class Person:
    # define constructor with name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create display method fro Person class
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)


# create child class Student of Person class
class Student(Person):
    # define constructor of Student class with section additional parameters
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    # Create display method for Student class
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)


# Testing Person class
P = Person("Tomas Wild", 37)
P.display()
S = Student("Albert", 23, "Mathematics")
S.displayStudent()