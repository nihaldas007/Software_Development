import tkinter as tk
import ttkbootstrap as ttk



app = ttk.Window(themename='solar')
app.geometry('300x150')
app.title('TypeWriter')

stringvar = tk.StringVar(value= 'Text')

label = ttk.Label(master=app, text='Text', textvariable=stringvar)
label.pack()

entry = ttk.Entry(master=app, textvariable=stringvar)
entry.pack();

entry2 = ttk.Entry(master=app, textvariable=stringvar)
entry2.pack();

app.mainloop()