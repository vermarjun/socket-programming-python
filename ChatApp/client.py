import socket

HOST = '192.168.43.127'
PORT = 9876

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

socket.send("Hello World".encode('utf-8'))

print(socket.recv(1024).decode('utf-8'))