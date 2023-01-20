######FICHIER MAIN.PY - FRONT USER############

###IMPORT###

import os
from pytube import YouTube
from pytube import Search
import sqlite3
import socket

###FONCTION###


def init(cur):
    cur.execute("CREATE table")
    cur.execute("CREATE table")
    cur.execute("CREATE table")



#FONCTION verification_utilisateur

def inscription(cursor,id,passwd):
    if not cursor.execute('SELECT * FROM user_table WHERE user_id =?',(id,)):
        cursor.execute('INSERT INTO user_table (user_id,user_passwd) VALUES (?,?)',(id,passwd))
        return True
    else:
        return False

def connexion_user(cur,id,passwd):
    if cur.execute('SELECT * FROM user_table WHERE user_id =? and user_name=?',(id,passwd)):
        return True
    return False


def aff_musique(cur):
    pass

def aff_musique_user(cur,user):
    pass

def add_musique(cur,nom_musique,username):
    # si la musique est présente dans la bdd
    # on renvoie le chemin

    # sinon: download_youtube.py
    # on ajoute la ligne dans la table MUSICS et users
    pass

def del_musique(cur,nom_musique,username):
    pass


#FONCTION connexion client serveur - socket

def client_program():
    host = '192.168.1.101'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" Sélectionner votre musique : ")  # take input

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Freezer : ' + data)  # show in terminal

        message = input("Lire une autre musique : ")  # again take input

    client_socket.close()  # close the connection


###PROGRAM###


connexion = sqlite3.connect("bdd_freezer.db")
cursor = connexion.cursor()



print("Bienvenue sur votre logiciel de musique open-source préféré !")
print("FREEZER !")

choix=input("Connexion ou Inscription? 1/2: ")


if choix== 1:
    print("Veuillez vous identifier")
    id_user = input("Identifiant utilisateur : ")
    passwd_user = input("Mot de passe : ")
    if  not connexion(cursor, id_user,passwd_user):
        print("Identifiants incorrect")
        exit()
elif choix == 2:
    print("Inscription")
    id_user = input("Identifiant utilisateur : ")
    passwd_user = input("Mot de passe : ")
    if not inscription(cursor,id_user,passwd_user):
        print("nom d'utilisateur deja prit")
        exit()


#le client est connecté




#os.system('su \'%' + id_user + '%\'')

if __name__ == '__main__':
     client_program()