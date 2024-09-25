import cv2
import socket
import pickle
import struct

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

# Data receiving function
def recvall(sock, count):
    buf = b''
    while count:
        new_buf = sock.recv(count)
        if not new_buf:
            return None
        buf += new_buf
        count -= len(new_buf)
    return buf

# Receive and display the streamed frames
while True:
    # Read the length of the data
    data_len = recvall(client_socket, struct.calcsize("L"))
    if not data_len:
        break
    # Unpack the data length and receive the data
    data_len = struct.unpack("L", data_len)[0]
    data = recvall(client_socket, data_len)
    # Deserialize the received data into a frame
    frame = pickle.loads(data)
    # Display the frame
    cv2.imshow('Stream', frame)
    # Wait for a key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the socket and destroy any OpenCV windows
client_socket.close()
cv2.destroyAllWindows()
