import tkinter as tk
import ttkbootstrap as ttk

def convert():
    input_value = entry_int.get()
    kilo_out = input_value * 1000
    output_string.set(kilo_out)


window = ttk.Window(themename='journal')
window.title("Convertion")
window.geometry('300x150')


head = ttk.Label(master = window, text='Gram to Kilogram', font = 'Calibri 24 bold')
head.pack()


frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=frame, textvariable=entry_int)
button = ttk.Button(master=frame, text='Convert', command = convert)
frame.pack(pady=10)
entry.pack(side='left', padx=10)
button.pack(side='left')


output_string = tk.StringVar()
output = ttk.Label(
    master=window, 
    text='Output', 
    font ='Calibri 24', 
    textvariable=output_string)
output.pack(pady=5)

window.mainloop()