import tkinter as tk 
import ttkbootstrap as ttk

app = ttk.Window(themename = 'vapor')
app.title('Buttons')
app.geometry('400x200')

def check():
    print(ch_var.get())
    ch_var.set(False)

ch_var = ttk.BooleanVar()
rad_var = ttk.StringVar()

A = ttk.Radiobutton(app,text='RadioA',value='A',command=check,variable=rad_var)
B = ttk.Radiobutton(app,text='RadioB',value='B',command=check,variable=rad_var)
check_button1 = ttk.Checkbutton(app, text='CheckButton1',command= lambda: print(rad_var.get()),variable=ch_var)

A.pack()
B.pack()
check_button1.pack()

app.mainloop()