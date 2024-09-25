import socket

# HOST = '192.168.43.127'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))
server.listen()

while True:
    communication_socket , address = server.accept()
    print(f'connected to {address}')
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from client is {message}')
    communication_socket.send(f"Got your message".encode('utf-8'))
    communication_socket.close()
    print(f'communication with {address} ended!')