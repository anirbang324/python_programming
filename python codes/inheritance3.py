class cookie:
    def banana(self):
        print("Today is a nice day")

class cake(cookie):
    def jam(self):
        print("It is cloudy today")

class grapes(cake):
    def bottle(self):
        pass

ob = grapes()
ob.banana()
ob.jam()
ob.bottle()
