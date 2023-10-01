import yt_dlp
from yt_dlp import YoutubeDL
import os

#getting the files directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# download options
dl_ops = {
    'outtmpl': os.path.join(current_directory, 'downloads', '%(uploader)s', '%(title)s.%(ext)s')
}

#downloading the video
videolink = input("Paste the video link: ")
with YoutubeDL(dl_ops) as ydl:
    ydl.download([videolink])
