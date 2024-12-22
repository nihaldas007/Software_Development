import pytube

download_path='C:/Users/Warning/Downloads'

link = input("Paste Your Link: ")
yt = pytube.YouTube(link)

yt.streams.first().download()
print("Video Downloaded")
