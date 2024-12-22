import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

app = ttk.Window(themename='darkly')
app.title('Robot Order')
app.geometry('900x200')
app.resizable(False, False)  # Allow resizing horizontally but not vertically
app.minsize(900, 200)

ico = Image.open('logo_roboon.jpg')
photo = ImageTk.PhotoImage(ico)
app.wm_iconphoto(False, photo)


bg = 'orange'
bg_font = 'black'
app.configure(background=bg)


def fun():
    table_number = num.get()
    food_name = food.get()
    mesage = f'The Robot Will the{food_name} on the table number{table_number}'
    print(f'The Robot Will the{food.get()} on the table number{num.get()}')



lebel = ttk.Label(app,text='Place an Order', font='Arial 15 bold italic',background=bg,foreground=bg_font).pack(side='top')
lebel1 = ttk.Label(app,text='Table Number:', font='Arial 12',background=bg, foreground=bg_font).pack(side='left', padx=20)
num= ttk.StringVar(value=0)
table = ttk.Spinbox(app, from_ = 1, to = 20, textvariable=num)
table.pack(side='left')

lebel2 = ttk.Label(app,text='Food Name:', font='Arial 12',background=bg, foreground=bg_font).pack(side='left', padx=20)

food = ttk.StringVar(value='Not Selected')
items = ['cake', 'ica cream', 'juice', 'nachos', 'Ramen']
combo = ttk.Combobox(app, textvariable=food)
combo.configure(values=items)
combo.pack(side='left',padx=20)

button = ttk.Button(app, 
                    text='Order', 
                    command=lambda:output.config(text= f'The robot will serve the {food.get()} at table number {num.get()}'),
                    )
button.pack(side='left')
button.bind('<FocusOut>')

output = ttk.Label(app,font='Arial 12 bold',
                    background=bg,
                    foreground=bg_font)
output.place(x=150,y=160)

app.mainloop()