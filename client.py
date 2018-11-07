"""
File: client.py
client-side application for doctor chat room
"""

from socket import *
from codecs import decode

HOST = "localhost"
PORT = 8000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)

print(decode(server.recv(BUFSIZE), CODE))       # The server's greeting
while True:
    message = input("> ")                       # Get my reply or quit
    if not message:
        break
    server.send(bytes(message, CODE))           # Send my reply to the server
    reply = decode(server.recv(BUFSIZE), CODE)  # Get the server's reply
    if not reply:
        print("Server disconnected")
        break
    print(reply)                                # Display the server's reply
server.close()
