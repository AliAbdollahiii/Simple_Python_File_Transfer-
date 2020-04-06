import socket
import sys,os,time

host = "127.0.0.1"
port = 9001

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

print("Socket Created")
file_name = input("Enter the filename: ")
sock.listen(1)
s,addr = sock.accept()
print("Client Connected From: {}".format(addr))

print("Sending File..")

message = file_name.encode("ascii")
s.sendall(message)
time.sleep(0.5)
with open(file_name,"rb") as reader:
    for line in reader:
        s.send(line)
    print("File Sent")
print("Socket Closing ..")
s.close()
sys.exit()    