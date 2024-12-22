import tkinter as tk
import ttkbootstrap as ttk

def button_fuc():
    text = entry.get()
    # update the label   
    label.config(text = text)
    entry['state'] = 'disabled'

def button_fun():
    text = entry.get()
    # update the label   
    label.config(text = 'Type Text')
    entry['state'] = 'enable'
    

root = ttk.Window(themename='solar')
root.geometry('300x150')
root.title('Widgets')

label = ttk.Label(master=root, text='Type Text')
label.pack()
entry = ttk.Entry(master=root)
entry.pack()
ttk.Button(master=root, text='Actived', command=button_fuc).pack(pady=2)

ttk.Button(master=root, text='Deactived', command=button_fun).pack()


root.mainloop()