import tkinter as tk
main_window = tk.Tk()
a1 = tk.Label(main_window, text="Hello Python", bg="red", fg="white",padx=20, pady=10, font="comicsansms 30 bold")
a1.pack()
# adding photo to our interface
# photo = tk.PhotoImage(file="img.png")
# label1 = tk.Label(image=photo)
# label1.pack()

main_window.mainloop()


