import jpysocket
import socket

host='127.0.0.1'
port=2001
s=socket.socket()
s.bind((host,port))
s.listen(5)
print("Socket Is Listening....")
connection,address=s.accept()
print("Connected To ",address)
msgsend=jpysocket.jpyencode("Thank You For Connecting.")
connection.send(msgsend)
data=connection.recv(1024)
for i in data:
    print(i)

s.close() #Close connection
print("Connection Closed.")