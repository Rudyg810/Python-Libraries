import tkinter as tk
import time as t
container = tk.Tk()
container.geometry("400x400")
def click2():
    if var.get() ==1:
        var2.set(0) 
    else:
        var2.set(1)

def click1():
    if var2.get() ==1:
        var.set(0) 
    else:
        var.set(1)
container.resizable(0,0)
container.title("Don't know TF")
entry = tk.Entry(container, width=300, borderwidth=5, justify="right") 
entry.place(x=0, y = 0)
var = tk.IntVar()
a = tk.StringVar()
Entry = tk.Entry( textvariable= a)
var = tk.IntVar()
var2 = tk.IntVar()
checkbox = tk.Checkbutton(container,width=10, text= "Celcius", command= click, variable=var)
checkbox.pack()
checkbox.place(x=145, y = 50)

checkbox2 = tk.Checkbutton(container,width=10, text= "Kelvin", variable=var2, command= click)
checkbox2.pack()
checkbox2.place(x= 141, y =  75)



container.mainloop()