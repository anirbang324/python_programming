import tkinter as tk
window = tk.Tk()
window.geometry("400x200")
label_1 = tk.Label(window, text = "label_1", bg="black", fg="white")
label_1.pack(side=tk.BOTTOM)
label_2 = tk.Label(window,text = "label_2", bg="black", fg="white")
label_2.pack(side=tk.TOP)
label_3 = tk.Label(window, text = "label_3", bg="black", fg="white")
label_3.pack(side=tk.LEFT)
label_4 = tk.Label(window,text = "label_4", bg="black", fg="white")
label_4.pack(side=tk.RIGHT)
window.mainloop()