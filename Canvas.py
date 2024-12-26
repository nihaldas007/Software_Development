import tkinter as tk
import ttkbootstrap as ttk

app = tk.Tk()
app.title('Canvas')
app.geometry('600x400')
app.resizable(False,False)


def movement(pos):
    x = pos.x
    y = pos.y
    color = val.get();
    print(color)
    canvas.create_oval((x-4/2,y-4/2,x-4/2,y-4/2),fill='red',width=3,outline=color)

#Canvas
canvas = tk.Canvas(app, bg='white')
canvas.pack()

item = ['red', 'black','green','blue']
val = tk.StringVar()
color_pick = ttk.Combobox(app, textvariable=val)
color_pick.pack()
color_pick.configure(value = item)
# canvas.create_rectangle((50,20,100,200), fill='red',width=2,dash=(1,2), outline='green')

# canvas.create_oval((100,100,200,200), fill='blue')
# canvas.create_arc((100,100,200,200), fill='red',start = 45, extent=140, style= tk.PIESLICE, outline ='green',width=1)
# canvas.create_polygon((0,0,100,100,200,200), fill='blue')
# canvas.create_text((100,200), text='Text is', fill='green',width=2)
# canvas.create_window((50,100), window= ttk.Label(app, text='text is'))

canvas.bind('<Motion>', movement)

app.mainloop()