# Project_Freezer
Freezer est un projet étudiant de plateforme de musique open-source

#########################################################################################################################################################################

V1 du projet :

Infrastructure : Une machine virtuelle dans les locaux du centre de formation fait office de serveur. Il possède comme service installé ProFTPD configuré en TLS, chaque utilisateur qui se connectera sera chrooter dans son home.

Code : un fichier main.py regroupe les fonctionnalités suivante : 

- Python socket pour la communication client serveur

- Téléchargement de vidéo youtube si la chanson sélectionné n'est pas dans le folder musique de l'user

- Création de l'utilisateur si ce dernier n'existe pas sur le serveur
