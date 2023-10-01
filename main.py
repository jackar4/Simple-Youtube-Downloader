import yt_dlp
from yt_dlp import YoutubeDL
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.realpath(__file__))

# Define the download options with the updated 'outtmpl' path
dl_ops = {
    'outtmpl': os.path.join(current_directory, 'downloads', '%(uploader)s', '%(title)s.%(ext)s')
}

videolink = input("Paste the video link: ")
with YoutubeDL(dl_ops) as ydl:
    ydl.download([videolink])
