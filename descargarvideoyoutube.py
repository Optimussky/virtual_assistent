# Este script aun no funciona correctamente
#Programa para descargar videos de youtube
# https://pytube.io/en/latest/

from fileinput import filename
from pytube import YouTube # pip install pytube
  
# where to save 
#SAVE_PATH = "." #to_do 
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=OG5L13AvKLM"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link).streams.first().download()
    yt = YouTube(link)
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
#d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename= 'GeeksforGeeks Video')
#mp4files = yt.streams.filter(file_extension='mp4')
#mp4files = yt.filter('mp4') 
  
#to set the name of the file
#yt.set_filename('GeeksforGeeks Video')  
  
# get the video with the extension and
# resolution passed in the get() function 
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename= 'GeeksforGeeks Video')
except: 
    print("Some Error!") 
print('Task Completed!')



"""
#Downloading multiple videos
from pytube import YouTube 
  
#where to save 
SAVE_PATH = "E:/" #to_do 
  
#link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=xWOoBJUqlbI", 
    "https://www.youtube.com/watch?v=xWOoBJUqlbI"
    ]
  
for i in link: 
    try: 
          
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(i) 
    except: 
          
        #to handle exception 
        print("Connection Error") 
      
    #filters out all the files with "mp4" extension 
    mp4files = yt.filter('mp4') 
  
    # get the video with the extension and
    # resolution passed in the get() function 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    try: 
        # downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!') 


# Download multiple videos using File Handling

from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
# opening the file
link=open('links_file.txt','r')

for i in link:
	try:
		
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
	except:
		
		#to handle exception
		print("Connection Error")
	
	#filters out all the files with "mp4" extension
	mp4files = yt.filter('mp4')
	
	# get the video with the extension and
	# resolution passed in the get() function
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		
		# downloading the video
		d_video.download(SAVE_PATH)
	except:
		print("Some Error!")
print('Task Completed!')







"""