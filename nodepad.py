import tkinter as tk
import ttkbootstrap as ttk

def btn() -> None:
    print('button pressed')

app = ttk.Window(themename='solar')
app.title('NotePad')
app.geometry('1080x720')


ttk.Label(master=app, text='Write the Text').pack()
ttk.Text(master=app, font= 'Calibri 12 bold').pack()
ttk.Entry(master=app).pack()
ttk.Button(master=app, text='A Button', command=btn).pack(pady=2)
ttk.Button(master=app, text='New Bee', command=btn).pack(pady=2)



app.mainloop()