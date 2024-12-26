import yt_dlp
import os
import time
import re
from datetime import datetime

def sanitize_filename(filename):
    """Sanitize the filename to ensure it works on Windows."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(url, quality, download_base_path):
    # Define the format based on the selected quality
    format_map = {
        '1080p': 'bestvideo[height=1080]+bestaudio/best',
        '720p': 'bestvideo[height=720]+bestaudio/best',
        '480p': 'bestvideo[height=480]+bestaudio/best',
        '320p': 'bestvideo[height=320]+bestaudio/best',
        'best': 'best',  # Default: best overall format
    }

    # Set the chosen format option
    format_choice = format_map.get(quality, 'best')  # Default to 'best' if invalid quality is selected

    # Define the output template with the custom path (without the month folder)
    ydl_opts = {
        'outtmpl': os.path.join(download_base_path, '%(title)s.%(ext)s'),  # Output location and filename
        'format': format_choice,         # Set the selected format
        'noplaylist': True,               # Avoid downloading playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Extract video info to get the actual title and file extension
        video_info = ydl.extract_info(url, download=False)
        title = sanitize_filename(video_info['title'])  # Sanitize the title to ensure valid characters

        # Find the actual file extension
        file_extension = video_info.get('ext', 'mp4')  # Default to 'mp4' if the extension is missing

        # Build the actual file path of the downloaded file
        downloaded_file_path = os.path.join(download_base_path, f"{title}.{file_extension}")

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

        print(f"Download complete! File saved to {downloaded_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage:
video_url = input("Enter the YouTube video URL: ")
quality = input("Enter the quality (1080p, 720p, 480p, 320p, or best): ").lower()

download_base_path = 'C:/Users/Warning/Downloads'


download_video(video_url, quality, download_base_path)

