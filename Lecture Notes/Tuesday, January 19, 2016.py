import socket

classSocket = socket.socket()
host = "woodhouse.ics.uci.edu"
port = 5151

classSocket.connect((host, port))
classSocket.send("FUCK CHINA\r\n".encode(encoding= 'utf-8'))
response_bytes = classSocket.recv(4096)
echo_socket_in = classSocket.makefile("r")  # pseudo file object
echo_socket_out = classSocket.makefile("w") # pseudo file object