# Programa que convierte un video a gif

from moviepy.editor import VideoFileClip

clip = VideoFileClip("videogracioso.mp4")
clip.write_gif("mygif.gif")
