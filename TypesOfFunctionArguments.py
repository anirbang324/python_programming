# Required arguments
def print_hello(name):
    print("Hello", name)


# Keyword arguments
def user_info(name, age):
    print("Hello", name, "Your age is : ", age)


# Default arguments
def user_info_default(name,age=10):
    print("Hello", name, "Your age is : ", age)

# Variable-length arguments
def greet(*name):
    for s in name:
        print("Hello", s)


print_hello("Python")
# print_hello()

user_info(age=20, name="Python")
user_info("Python", 20)
user_info(20, "Python")

user_info_default("Python Default", 20)
user_info_default("Python Default")

greet("Python")
greet("Python", "Java", "C++", "Ruby")
