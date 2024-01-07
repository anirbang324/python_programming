from abc import *
class C(ABC):
    @abstractmethod #instructing the interprter that p is a abstract method
    def p(self):
        pass

class A(C):
    def p(self):
        print("hello")
#c1= C()
c2 =A()
c2.p()

