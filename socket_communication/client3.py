#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()      
print(f"Host name: {host}")              

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

while True:
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    print (msg.decode('ascii'))

    # get text from user
    client_msg = input("Message: ")

    # send message to server
    s.send(client_msg.encode('ascii'))

    if client_msg == "q":
        s.close()
        break
        
                           
