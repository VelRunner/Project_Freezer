#!/usr/bin/python

import socket

def server_program():
    host = '192.168.1.101'  #socket.gethostname() # get the hostname
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(10)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input('Envoie de la musique... ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
    server_socket.close() # close the socket

if __name__ == '__main__':
    server_program()

