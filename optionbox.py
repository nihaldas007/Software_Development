import tkinter as tk
import ttkbootstrap as ttk

def fodi():
    print(food.get())

app = ttk.Window(themename='vapor')
app.title('Combobox')
app.geometry('400x200')

items = ['Cake', 'French Fry', 'Ice Cream']
food = tk.StringVar(value='None')
combo = ttk.Combobox(app, textvariable=food)
combo.configure(values = items)
combo.pack(pady=20);

combo.bind('<<ComboboxSelected>>', lambda event: print(food.get()))

num = ttk.IntVar(value=0)
spin = ttk.Spinbox(app, from_ = 1,to = 20,command= lambda: print(num.get()), textvariable=num)
# spin['values'] = (1,2,3,4,5)
spin.pack()

spin_char = ttk.StringVar()
spin = ttk.Spinbox(app,command= lambda: print(spin_char.get()), textvariable=spin_char)
spin['values'] = ('A','B','C','D','E')
spin.pack()


app.mainloop()