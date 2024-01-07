# return <expression/value>

def addition(a, b):
    return a + b


def demo(a, b):
    return a + b, a - b


add = addition(10, 20)
print(add)

add, sub = demo(5, 3)
print(add)
print(sub)
