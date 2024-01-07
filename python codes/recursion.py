i = 0 #global variable

def func1():
    global i  #global variable
    i+=1
    print("hi",i)  #996 lines
    func1()

func1()

