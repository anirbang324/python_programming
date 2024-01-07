import tkinter as tk

main_window = tk.Tk()
main_window.title("button")
main_window.geometry("400x300")
button1 = tk.Button(main_window, text="click Here", height=4, width=10)
button1.grid(row=1, column=1)
main_window.mainloop()

