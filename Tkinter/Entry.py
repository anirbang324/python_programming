import tkinter as tk
main_window = tk.Tk()
main_window.geometry("500x300")
entry = tk.Entry(main_window, fg="red", justify="center",font="Ariel 16 ", bd=4)
entry.pack()
main_window.mainloop()

