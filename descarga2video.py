# Este script si funciona correctamente
from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=OG5L13AvKLM').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=OG5L13AvKLM')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()