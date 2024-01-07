#hybrid inheritance

class level1:
    def printvalue(self):
        print("this is level 1 parent class")
class level2(level1):  # multilevel inheritance
    def printvalue2(self):
        print("this is level 2 parent class")
class level3(level2,level1):  #multiple inheritance
    def printvalue3(self):
        print("this is level 3 class")

object = level3()
object.printvalue2()