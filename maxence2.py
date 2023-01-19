# Installation du module : pytube

from pytube import YouTube 

#Import du module vlc

import vlc

url = input("Veuillez rentrer l'url de la musique :  ")

def on_dowload_progress(stream, chunk, bytes_remaining):
    bytes_dowloaded = stream.filesize - bytes_remaining
    percent = bytes_dowloaded * 100 / stream.filesize
    print(f"Progression du téléchargement {int(percent)}%")


youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_dowload_progress)

print("TITRE: " + youtube_video.title)

stream = youtube_video.streams.get_by_itag(139)
print("Téléchargement...")
stream.download()
print("OK")

#Lien dynamique 
s = Search(input("Veuillez entrer la musique de votre choix : "))
len(s.resultats)
s.resultats[1]
https://www.youtube.com/watch?v={videoid}

