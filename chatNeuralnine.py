# chat en tkinter
# URL =  https://www.youtube.com/watch?v=sopNW98CRag&list=PLb-T35byRj_8_YywqOi8DvNxm6rbmMCNI&index=3
#from email import message
import socket
import threading
HOST = '192.168.85.1'
PORT = 9090

# Basic settings for a Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []

nicknames = []

# make 3 functions

#broadcast (send messages to every client connected)
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # this is only a message for the server
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]
            nicknames.remove(nickname)
            break

#receive ()
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname} ")
        broadcast(f"{nickname} connected to the server! \n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))



        thread = threading.Thread(target=handle, args=(client,))
        thread.start()





#handle
print("Server is running")
receive()
