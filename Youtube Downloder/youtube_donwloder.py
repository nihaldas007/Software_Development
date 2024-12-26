import tkinter as tk
import ttkbootstrap as ttk
import yt_dlp
import os
import time
import re  # For sanitizing the filename



def sanitize_filename(filename):
    """Sanitize the filename to ensure it works on Windows."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# For download the video
def download_video():
    link = link_var.get()
    resulation = res.get()
    download_path = 'C:/Users/Warning/Downloads'
    format_map = {
        '1080p': 'bestvideo[height=1080]+bestaudio/best',
        '720p': 'bestvideo[height=720]+bestaudio/best',
        '480p': 'bestvideo[height=480]+bestaudio/best',
        '320p': 'bestvideo[height=320]+bestaudio/best',
        'best': 'best',  # Default: best overall format
    }
    # Set the chosen format option
    format_choice = format_map.get(resulation, 'best')  # Default to 'best' if invalid quality is selected

    # current_month = datetime.now().strftime("%B-%Y")

    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output filename template
        'format': format_choice,  # Download the best video + best audio, fallback to best if combined isn't available
        'noplaylist': True,  # Avoid downloading playlists
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            video_info = ydl.extract_info(link, download=False)

        title = sanitize_filename(video_info['title'])  # Sanitize the title to ensure valid characters

        # Find the actual file extension
        file_extension = video_info.get('ext','mp4')  # Default to 'mp4' if the extension is missing

        # Build the actual file path of the downloaded file
        downloaded_file_path = os.path.join(download_path, f"{title}.{file_extension}")

        # Normalize the path to ensure correct file path format
        downloaded_file_path = os.path.normpath(downloaded_file_path)

        # Check if the downloaded file exists
        if not os.path.exists(downloaded_file_path):
            print(f"Error: {downloaded_file_path} not found!")
            return

        # Get the current time (the time of the download)
        current_time = time.time()

        # Set the access and modification times to the current time
        os.utime(downloaded_file_path, (current_time, current_time))
        print("Download complete!")
        # tir = True
        down_label.config(text='Download complete!')
        down_label.after(2000, down_label.destroy)
    except Exception as e:
        print(f"Error: {e}")
#Entry system
def on_entry_click(event):
    if entry.get() == "paste the video link here":  # Default text
        entry.delete(0, tk.END)  # Clear the text

# Application GUI Started 
app = ttk.Window(themename='darkly')
app.title('Youtube Video Downloader')
app.geometry('950x550')
app.resizable(False, False)  # Allow resizing horizontally but not vertically
# app.minsize(1000, 200)

heading = ttk.Label(app, text='Video Downloader', font='Arial 12 bold',foreground='red').place(x = 0, y = 0)

img = tk.PhotoImage(file="D:/VS Code 2024/Software_Development/Youtube Downloder/social.png")
#Link Paste Section
label = ttk.Label(app, image= img).place(x = 220, y = 0)
link_var = ttk.StringVar()
entry = ttk.Entry(app,width=50,textvariable=link_var)
entry.place(x=80, y=450)  # Center of the window
entry.insert(0, "paste the video link here")

entry.bind("<FocusIn>", on_entry_click)  # Clear text when clicked

#Quality Selection
items = ['Best','1080p', '720p', '480p', '320p']
res = ttk.StringVar(value='Best')
quality = ttk.Combobox(app,textvariable=res)
quality.place(x=550,y=450)
quality.configure(value=items)

#Dowmload Section
def press():
    download_video()
        

download = ttk.Button(text='Download', bootstyle='btn-outline-primary', command=press)
download.place(x=763,y=450)

down_label = ttk.Label(app)
down_label.place(x=420,y=500)


app.mainloop()