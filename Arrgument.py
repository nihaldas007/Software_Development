import tkinter as tk
import ttkbootstrap as ttk
 
app = ttk.Window(themename='solar')
app.geometry('600x400')
app.title('Arrguments')

def button_func(entry_string):
    print('button pressed')
    print(entry_string.get())

entry_string = tk.StringVar(value= 'text')
entry = ttk.Entry(app, textvariable=entry_string)
entry.pack(pady=20)

button = ttk.Button(app, text='Butoon', command= lambda: button_func(entry_string))
button.pack()


app.mainloop()