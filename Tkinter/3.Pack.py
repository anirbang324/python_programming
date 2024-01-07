import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")

label_1 = tk.Label(main_window, text="Hello Python 1", bg="green", fg="white",font = 300)
label_1.pack(side=tk.BOTTOM)

label_2 = tk.Label(main_window, text="Hello Python 2", bg="green", fg="white",font = 300)
label_2.pack(side=tk.TOP)

label_3 = tk.Label(main_window, text="Hello Python 3", bg="green", fg="white",font = 300)
label_3.pack(side=tk.LEFT, fill=tk.Y)

# padx and pady
label_4 = tk.Label(main_window, text="Hello Python 4", bg="blue", fg="white",font = 300)
label_4.pack(pady=10)

label_5 = tk.Label(main_window, text="Hello Python 5", bg="blue", fg="white",font = 300)
label_5.pack(pady=10)

label_6 = tk.Label(main_window, text="Hello Python 6", bg="blue", fg="white",font = 300)
label_6.pack(side=tk.LEFT, padx=10)

label_7 = tk.Label(main_window, text="Hello Python 7", bg="blue", fg="white",font = 300)
label_7.pack(side=tk.LEFT, padx=10)

label_8 = tk.Label(main_window, text="Hello Python 8", bg="blue", fg="white",font = 300)
label_8.pack(padx=10, ipadx=10, ipady=10)

label_9 = tk.Label(main_window, text="Hello Python 9", bg="blue", fg="white",font = 300)
label_9.pack(ipadx=10)

main_window.mainloop()
