#https://www.altaruru.com/descargar-videos-y-musica-de-youtube-con-python-pytube/

import pytube
import time
from tqdm import tqdm



url="https://www.youtube.com/watch?v=mMezRFzwBws"
#path="/home/nuse/Descargas/pytube"

yt = pytube.YouTube(url)
 
print("Titulo .........: " + yt.title)
print("Duracion (seg)..: " + str(yt.length))
print("Descripcion.....: " +  yt.description)


try:
    yt.streams.filter(progressive=True, file_extension='mp3').order_by('resolution').desc().first().download()
    #lstst=yt.streams.filter(only_audio=True).download()
    for st in lstst:
        print(st)
except:
    try:
        #lstst=yt.streams.filter(only_audio=True).download()
        audio = yt.streams.get_audio_only().download()
        audioclip = AudioFileClip(audio)
        audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
 
        os.remove(audioclip.filename)
        for st in audio:
            print(st)
    except:
        print("Ocurrió algún problema con la descarga")

for i in tqdm(range(1000),desc="Esta es mi progressbar y describe... nada"):
    time.sleep(0.01)