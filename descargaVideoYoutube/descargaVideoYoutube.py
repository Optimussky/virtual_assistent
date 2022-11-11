#https://www.altaruru.com/descargar-videos-y-musica-de-youtube-con-python-pytube/
#pip install pytube
#pip install tqdm
import pytube
import time
from tqdm import tqdm



url="https://www.youtube.com/watch?v=ltt-T5IRFaw"
#path="/home/nuse/Descargas/pytube"

yt = pytube.YouTube(url)
 
print("Titulo .........: " + yt.title)
print("Duracion (seg)..: " + str(yt.length))
print("Descripcion.....: " +  yt.description)


try:
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().captions.get_by_language_code('en')
    lstst=yt.streams.filter('mp4').set_filename(yt.title+"getting").download()
    for st in lstst:
        print(st)
except:

    print("Ocurrió algún problema con la descarga")

for i in tqdm(range(1000),desc="Esta es mi progressbar y describe... nada"):
    time.sleep(0.01)