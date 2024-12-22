import tkinter as tk
import ttkbootstrap as ttk

def on_entry_click(event):
    """Clears the entry widget when clicked."""
    if entry.get() == "paste the video link here":  # Default text
        entry.delete(0, tk.END)  # Clear the text


app = ttk.Window(themename='vapor')
app.title('Youtube Downloader')
app.geometry('800x200')
app.resizable(False, False)  # Allow resizing horizontally but not vertically
app.minsize(1000, 200)

#Link Paste Section
entry = ttk.Entry(app,width=50)
entry.place(x=80, y=80)  # Center of the window
entry.insert(0, "paste the video link here")

entry.bind("<FocusIn>", on_entry_click)  # Clear text when clicked

#Quality Selection
items = ['1080p', '720p', '480p', '320p']
quality = ttk.Combobox(app)
quality.place(x=550,y=80)
quality.configure(value=items)

#Dowmload Section
download = ttk.Button(text='Download', bootstyle='btn-outline-primary')
download.place(x=763,y=80)




app.mainloop()