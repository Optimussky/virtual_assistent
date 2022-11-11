# Este script si funciona correctamente
import pytube
from pytube import YouTube
import time
from tqdm import tqdm

URL = "https://www.youtube.com/watch?v=mMezRFzwBws"
try:
    YouTube(URL).streams.first().download()
    yt = YouTube(URL)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Titulo .........: " + yt.title)
    print("Duracion (seg)..: " + str(yt.length))
    print("Descripcion.....: " +  yt.description)
except:
    #https://neuralcovenant.com/2020/09/25/descargar-video-o-audio-de-youtube-usando-python/
    try:
        yt = YouTube(URL)
        audio = yt.streams.get_audio_only().download()
        audioclip = AudioFileClip(audio)
        audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
 
        os.remove(audioclip.filename)
        #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        import time
        from tqdm import tqdm

        for i in tqdm(range(1000),desc="Esta es mi progressbar y describe... nada"):
            time.sleep(0.01)
    except:
        print("Ocurrió algún problema en el tiempo de ejecución")