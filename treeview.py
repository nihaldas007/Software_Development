import tkinter as tk
import ttkbootstrap as ttk
from random import choice

app = ttk.Window(themename = 'vapor')
app.title('TreeView')
app.geometry('800x600')
app.resizable(False, False)

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henrry', 'Lisa', 'Anna', 'Isha']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(app, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='Email')
table.pack(fill='both',expand=True)

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@email.com'
    data = (first,last,email)
    table.insert(parent='',index=0,values=data)
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])


table.bind('<<TreeviewSelect>>', item_select)

app.mainloop()