from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

#download data and config
download_options = {
    'format' : 'bestaudio/best',
    'outtmpl' : '%(title)s.%(ext)s',
    'nocheckcertificate' : True,
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192',
    }]
}

#checks song dir
if not os.path.exists('Songs'):
    os.mkdir('Songs')
else:
    os.chdir('Songs')

#Downloads songs
with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + argv[1], 'r') as f:
        for song_url in f:
            dl.download([song_url])