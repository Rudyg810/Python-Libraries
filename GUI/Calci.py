import tkinter as tk
container = tk.Tk()
container.geometry("400x400")
container.resizable(0,0)
container.title("Calci")
container.configure(bg = "grey")
a = tk.StringVar()
e1 = tk.Entry(container, font=("Arial", 25), justify= "right", textvariable=a)
e1.place(x=0,y=0, width="400", height= 50)

b1 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b1.place(x =5, y = 100, width=100, height=100)

b2 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b2.place(x =105, y = 100, width=100 , height=100) 
b3 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b3.place(x =205, y = 100, width=100, height=100)
b10 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b10.place(x =305, y = 100, width=100, height=100)
b4 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b4.place(x =5, y = 200, width=100,height=100)
b5 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b5.place(x =105, y = 200, width=100, height=100)
b6 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b6.place(x =205, y = 200, width=100 , height=100)
b11 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b11.place(x =305, y = 200, width=100, height=100)
b7 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b7.place(x =5, y = 300, width=100, height=100)
b8 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b8.place(x =105, y = 300, width=100, height=100)
b9 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b9.place(x =205, y = 300, width=100, height=100)
b12 = tk.Button(container, text="7", font= ("Arial", 25), fg="black", bg= "gray")
b12.place(x =305, y = 300, width=100, height=100)
container.mainloop()