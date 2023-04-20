!//usr/bin/python
 
import socket
ip =input ("enter the IP address: ")
port = input ("Enter the port Number: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if sock.connect_ex((ip,port)):
        print ("Port ",port, "is closed")
else:
        print ("port",port, "is OPEN")
