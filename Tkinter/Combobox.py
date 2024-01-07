#write a tkinter program to implement a combobox that will show 4 countries and you can choose among them.

import tkinter as tk
import tkinter.ttk as ttk
main_window = tk.Tk()
main_window.geometry("250x250")
combo_box1 = ttk.Combobox(main_window)
combo_box1['values'] = [1, 2, 3]
combo_box1.current(1)
combo_box1.pack()
main_window.mainloop()
