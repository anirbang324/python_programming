import tkinter as tk
import math
main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry("250x400")

expression = ""  #global variable

def key_press(key):
    global expression
    expression = expression + str(key)
    input_text.set(expression)

def key_clear():
    global expression
    expression = "" 
    input_text.set(expression)   #setting it to empty

def key_equal():
    result = eval(expression)
    input_text.set(result)

def fac():
    t=expression_field.get()
    t=int(t)
    r=math.factorial(t)
    input_text.set(r)

def sin():
    a=expression_field.get()
    a=int(a)
    result=math.sin(a)
    input_text.set(result)

input_text = tk.StringVar()
expression_field = tk.Entry(main_window, font="Ariel 16 bold", justify="left",
                            textvariable=input_text)
expression_field.grid(row=1, column=1, columnspan=8, ipadx=70)

button1 = tk.Button(main_window, text="1", height=4, width=2,bg="bisque2",command=lambda: key_press("1"))
button1.grid(row=2, column=1, sticky="nsew") #north,south,east,west

button2 = tk.Button(main_window, text="2", height=4, width=2,bg="bisque2",command=lambda: key_press("2"))
button2.grid(row=2, column=2, sticky="nsew")

button3 = tk.Button(main_window, text="3", height=4,width=2,bg="bisque2",command=lambda: key_press("3"))
button3.grid(row=2, column=3, sticky="nsew")

button4 = tk.Button(main_window, text="4", height=4, width=2,bg="bisque2",command=lambda: key_press("4"))
button4.grid(row=3, column=1, sticky="nsew")

button5 = tk.Button(main_window, text="5", height=4, width=2,bg="bisque2",command=lambda: key_press("5"))
button5.grid(row=3, column=2, sticky="nsew")

button6 = tk.Button(main_window, text="6", height=4, width=2,bg="bisque2",command=lambda: key_press("6"))
button6.grid(row=3, column=3, sticky="nsew")

button7 = tk.Button(main_window, text="7", height=4, width=2,bg="bisque2",command=lambda: key_press("7"))
button7.grid(row=4, column=1, sticky="nsew")

button8 = tk.Button(main_window, text="8", height=4, width=2,bg="bisque2",command=lambda: key_press("8"))
button8.grid(row=4, column=2, sticky="nsew")

button9 = tk.Button(main_window, text="9", height=4, width=2,bg="bisque2",command=lambda: key_press("9"))
button9.grid(row=4, column=3, sticky="nsew")

button_zero = tk.Button(main_window, text="0", height=4, width=2,bg="bisque2",command=lambda: key_press("0"))
button_zero.grid(row=5, column=1, sticky="nsew")

button_clear = tk.Button(main_window, text="Clear", height=4, width=2,bg="darkslategray1", command=key_clear)
button_clear.grid(row=5, column=2, sticky="nsew")

# button_equal = tk.Button(main_window, text="=", height=4, width=2)
# button_equal.grid(row=5, column=3, sticky="nsew")

button_plus = tk.Button(main_window, text="+", height=4, width=2,bg="darkslategray1",command=lambda: key_press("+"))
button_plus.grid(row=2, column=4, sticky="nsew")

button_minus = tk.Button(main_window, text="-", height=4, width=2,bg="darkslategray1",command=lambda: key_press("-"))
button_minus.grid(row=3, column=4, sticky="nsew")

button_divide = tk.Button(main_window, text="/", height=4,width=2,bg="darkslategray1",command=lambda: key_press("/"))
button_divide.grid(row=5, column=4, sticky="nsew")

button_multiply = tk.Button(main_window, text="*", height=4, width=2,bg="darkslategray1",command=lambda: key_press("*"))
button_multiply.grid(row=4, column=4, sticky="nsew")

button_equal = tk.Button(main_window, text="=", height=4, width=2, bg="darkslategray1",command=key_equal)
button_equal.grid(row=5, column=3, sticky="nsew")

button_fact = tk.Button(main_window, text="!", height=4,bg="darkslategray1", width=2, command=fac)
button_fact.grid(row=6, column=4, sticky="nsew")

button_sin = tk.Button(main_window, text="sin", height=4,bg="darkslategray1", width=2, command=sin)
button_sin.grid(row=6, column=3, sticky="nsew")

main_window.mainloop()
