class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        print('This Department class is inherited from Employee')

dept = Department()
dept.message()