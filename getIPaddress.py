import socket
hostname = socket.gethostname()
myIP = socket.gethostbyname(hostname)
print(f"Mi IP es: {myIP}")