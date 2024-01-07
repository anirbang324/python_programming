class sub:
    def __init__(self):
        self.a=int(input())
        self.b=int(input())
        self.c=self.a-self.b

    def multi1(self):
        self.d=self.a*self.b

    def print(self):
      print(self.c)
      print(self.d)

object=sub()
object.print()