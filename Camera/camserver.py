import socket
import cv2
import struct
import pickle

# SOCKET CREATE:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

# SOCKET BIND:
server_socket.bind((HOST,PORT))

# SOCKET LISTEN:
server_socket.listen(5)
print(f"Listening At: {HOST}, {PORT}")

# ACCEPT A CLIENT CONNECTION
client_socket, addr =  server_socket.accept()
print(f"Got connection form: {addr}")

# Capturing Video Frame using CV2:
vid = cv2.VideoCapture(0)
    

# SOCKET ACCEPT:
while True:
    # READING FRAMES FROM CAMERA
    img, frame = vid.read()
    # USING PICKLE TO SERIALIZE FRAMES TO BYTE DATA
    data = pickle.dumps(frame)
    # PACKING EACH FRAME DATA USNG STRUCT MODULE
    message = struct.pack("L",len(data))+data

    # SENDING THIS PACKED DATA TO CLIENT:
    client_socket.sendall(message)

    # Wait for a key press and break the loop if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the camera and close the sockets
vid.release()
client_socket.close()
server_socket.close()

