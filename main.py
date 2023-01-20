######FICHIER MAIN.PY - FRONT USER############

###IMPORT###

import os
from pytube import YouTube
from pytube import Search
import sqlite3
import socket

###FONCTION###

#FONCTION verification_utilisateur

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


print("Bienvenue sur votre logiciel de musique open-source préféré !")
print("FREEZER !")
print("Veuillez vous identifier")
id_user = input("Identifiant utilisateur : ")
passwd_user = input("Mot de passe : ")

connexion = sqlite3.connect("bdd_freezer.db")
cursor = connexion.cursor()

verif_identifiant(id_user,passwd_user)

os.system('su \'%' + id_user + '%\'')

if __name__ == '__main__':
     client_program()