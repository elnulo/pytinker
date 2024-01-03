import tkinter as tk


print ("Hello World")
master = tk.Tk()
master.title("Hello World")

l1 = tk.Label(master, text="First Label")
l1.grid(column=0, row=0, sticky = tk.W, pady = 2)

l2 = tk.Label(master, text="Second Label")
l2.grid(column=0, row=1)

e3 = tk.Entry(master)
e3.grid(column=1, row=0)
tk.mainloop()
