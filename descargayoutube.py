from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=OG5L13AvKLM")
print(yt.title)
stream = yt.streams.first()
stream.download()