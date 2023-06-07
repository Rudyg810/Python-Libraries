import tkinter as tk
container = tk.Tk()
container.geometry("400x400")
container.resizable(0,0)
container.title("Combo")
container.configure(bg = "grey")
lang1 = tk.IntVar()
lang2 = tk.IntVar()
lang3 = tk.IntVar()
lang4 = tk.IntVar()

def click():
    a = lang1.get()
    b = lang2.get()
    c = lang3.get()
    d = lang4.get()


chk_C= tk.Checkbutton(container, text="C", variable=lang1, command=click)
chk_Cplus= tk.Checkbutton(container, text="C++", variable=lang2, command=click)
chk_Csharp= tk.Checkbutton(container, text="C#", variable=lang3, command=click)
chk_Swift= tk.Checkbutton(container, text="Swift", variable=lang4, command=click)

container.mainloop()