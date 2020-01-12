#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()    
print(f"Host name: {host}")                  

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(3)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   server_msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(server_msg.encode('ascii'))

   client_msg = clientsocket.recv(1024)
   client_msg = str(client_msg.decode("ascii"))
   print(client_msg)
   if client_msg == "stop":
       serversocket.close()
       break

   clientsocket.close()