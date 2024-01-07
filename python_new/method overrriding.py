class parent:
    def function(self):
        print("parent class's method")
class child(parent):
    def function(self):
        print("child class's method")
ob = child()
ob.function()