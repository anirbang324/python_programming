#multilevel inheritance

class level1:
    def printvalue(self):
        print("this is level 1 parent class")
class level2(level1):
    def printvalue2(self):
        print("this is level 2 parent class")
class level3(level2):
    def printvalue3(self):
        print("this is level 3 class")
obj = level3()
obj.printvalue()
obj.printvalue2()
obj.printvalue3()