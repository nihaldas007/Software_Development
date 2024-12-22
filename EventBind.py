import tkinter as tk
import ttkbootstrap as ttk

def get_pos(pos):
    print(f'x:{pos.x} y:{pos.y}')


app = ttk.Window(themename='darkly')
app.title('Event Binding')
app.geometry('800x600')

text = ttk.Text(app, font='Arial 10 italic bold')
text.pack()

entry = ttk.Entry(app, font='Arial 10 italic bold')
entry.pack()

button = ttk.Button(app, text='Button', command= lambda: print('Button Pressed'))
button.pack()

# button.bind('<Alt-KeyPress-a>', lambda event: print('An Event'))
# app.bind('<Motion>', get_pos)

text.bind('<Enter>', lambda event: print('MouseWheel'))
# entry.bind('<FocusOut>', lambda event: print(event))
app.mainloop()