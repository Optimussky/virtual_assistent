import pytube
from pytube import YouTube 
  
#https://pytube.io/en/latest/user/streams.html
URL="https://www.youtube.com/watch?v=mMezRFzwBws"
try:
    yt = YouTube(URL,on_progress_callback=progress_func,on_complete_callback=complete_func,proxies=my_proxies,use_oauth=False,allow_oauth_cache=True).download()
    #caption = yt.captions.get_by_language_code('en')
    
    
except:
    print('Ha ocurrido algún tipo de error')
print('Task Completed!') 