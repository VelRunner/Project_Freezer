# Installation du module : pytube
from pytube import YouTube 
from pytube import Search

# Importation des modules os
import os.path
import os

#Variable s qui permet de rechercher via la fonction Search
s = Search(input("Veuillez entrer la musique de votre choix : "))

#Récupération de l'id de la vidéo exemple:IA0HNreJ8fg
lien = s.results[0].video_id

#Addition du lien + id pour avoir le lien complet de la musique
url = "https://www.youtube.com/watch?v=" + lien

#Fonction pour une afficher la progression
def on_dowload_progress(stream, chunk, bytes_remaining):
    bytes_dowloaded = stream.filesize - bytes_remaining
    percent = bytes_dowloaded * 100 / stream.filesize
    print(f"Progression du téléchargement {int(percent)}%")

#Recherche sur youtube via l'url
youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_dowload_progress)

#Affichage du titre de la vidéo qui va être téléchargé
print("TITRE: " + youtube_video.title)

#Choix du format .mp4 via l'itag 139
stream = youtube_video.streams.get_by_itag(139)

print("Téléchargement...")

#Condition afin de créer ou non le fichier musique et le télécharger dedans
if os.path.isdir('/home/mduchilier/Project_Freezer/Musique'):
    print("Dossier Musique trouvé, la musique va se télécharger dedans ..")
    #Changement de répertoire
    os.chdir('/home/mduchilier/Project_Freezer/Musique')
else:
    print("Dossier Musique non trouvé, création du dossier Musique ..")
    #Création du dossier musique
    os.mkdir('Musique')
    #Changement de répertoire
    os.chdir('/home/mduchilier/Project_Freezer/Musique')

#Téléchargement de la musique
stream.download()

#Affichage de OK pour signaler la fin du téléchargement
print("OK")

