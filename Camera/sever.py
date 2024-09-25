import cv2
import socket
import pickle
import struct

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(10)

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection from: {client_address}")

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Serialize the frame
    data = pickle.dumps(frame)

    # Pack the serialized data and send it over the network
    client_socket.sendall(struct.pack("L", len(data)) + data)

    # Wait for a key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the sockets
cap.release()
client_socket.close()
server_socket.close()
