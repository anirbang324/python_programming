class Addition:
    # Defininf a constructor
   def __init__(b):
        b.num1=int(input("Enter your number:"))
        b.num2=int(input("Enter your number:"))
        b.num3=int(input("Enter your number:"))

   def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:',self.num)


# Here we create the object for call
# which calls the constructor
ob1 = Addition()

# calling the instance method
# using the object Sum
ob1.result()