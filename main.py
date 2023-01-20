######FICHIER MAIN.PY - FRONT USER############

###IMPORT###

import os
from pytube import YouTube
from pytube import Search
import sqlite3

###FONCTION###

def verif_identifiant(id,passwd):
    if id != cursor.execute('SELECT * FROM user_table WHERE user_id = \'%' + id + '%\''):
        true = input("Votre nom d'utilisateur n'existe pas dans la base de donnée, êtes-vous un nouvel utilisateur (exit pour sortir du programme)?")
        if true != 'exit':
            print("Inscription")
            id = input("rentrer votre identifiant")
            passwd = input("rentrer votre mot de passe")
            cursor.execute('INSERT INTO user_table (user_id,user_passwd) VALUES \'%' + id,passwd + '%\'')
            os.system('sudo adduser \'%' + id + '%\'')
            os.system('sudo passwd \'%' + id, passwd + '%\'')
            print("vous être maintenant inscrit")
        else:
            print("au revoir")
            exit()
    else:
        print("Bienvenue ",id)



###PROGRAM###


print("Bienvenue sur votre logiciel de musique open-source préféré !")
print("FREEZER !")
print("Veuillez vous identifier")
id_user = input("Identifiant utilisateur : ")
passwd_user = input("Mot de passe : ")

connexion = sqlite3.connect("bdd_freezer.db")
cursor = connexion.cursor()

verif_identifiant(id_user,passwd_user)
