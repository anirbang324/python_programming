import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")

for i in range(4):
    for j in range(4):
        label = tk.Label(main_window, text="Python", bg="blue", fg="white")
        label.grid(row=i, column=j, padx=2, pady=2)

main_window.mainloop()
