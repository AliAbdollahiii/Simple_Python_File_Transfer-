import socket
import sys,os,time

server = "127.0.0.1"
port = 9001

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((server,port))
print("Connected to Server!")

data = sock.recv(1024)
file_name = data.decode("ascii")
print("Receiving File: {}".format(file_name))
time.sleep(0.5)
with open(file_name,"wb") as writer:
    data = sock.recv(1024)
    while data:
        writer.write(data)
        data = sock.recv(1024)
    print("File Received Successfully!")
sock.close()
print("Closing..")
sys.exit()