import tkinter as tk
from tkinter import ttk
cont = tk.Tk()
cont.geometry("300x300")
menu = tk.Menu(cont)
sub = tk.Menu(cont)
menu.add_cascade(label= "windows", menu= subm  )
sub.add_command(label= "Start")
cont.config(menu = menu)
cont.mainloop()