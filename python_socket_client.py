#!/usr/bin/python

import socket

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


if __name__ == '__main__':
     client_program()
