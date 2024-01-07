class Student:
    roll_num = 9132 #instance variable
    name = "Ani" #instance variable
    def display(self):
        print(self.roll_num, self.name)

st = Student()
st.display()