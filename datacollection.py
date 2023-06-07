import tkinter as tk

container = tk.Tk()
container.geometry("400x800")

seg1 = tk.LabelFrame(container, text="Personal Details", borderwidth=2, bg="grey", height=300)
seg1.pack(fill="both", expand=True)
a1= tk.Label(seg1, text='Name  ').grid(row=0,column=0, pady=2, padx= 5, )
a2= tk.Label(seg1, text='Age   ').grid(row=1,column=0, pady=2, padx= 5)
a3= tk.Label(seg1, text='Sex   ').grid(row=2,column=0, pady=2, padx= 5)
a4= tk.Label(seg1, text='Mail  ').grid(row=3,column=0, pady=2, padx= 5)
a5= tk.Label(seg1, text='Number').grid(row=4,column=0, pady=2, padx= 5)

b1= tk.Entry(seg1, ).grid(row=0,column=1, pady=2, padx= 5)
b2= tk.Entry(seg1).grid(row=1,column=1, pady=2, padx= 5)
b4= tk.Entry(seg1, ).grid(row=3,column=1, pady=2, padx= 5)
b5= tk.Entry(seg1).grid(row=4,column=1, pady=2, padx= 5)
seg2 = tk.LabelFrame(container, text="Segment 2", borderwidth=2, bg="white", height=500)
seg2.pack(fill="both", expand=True)


gender = tk.IntVar
male_radio = tk.Radiobutton(seg1, text="M", variable=gender, value=0, ).grid(row=2, column=1 )

female_radio = tk.Radiobutton(seg1, text="F", variable=gender, value=1  ).grid(row=2, column=2)

container.mainloop()
