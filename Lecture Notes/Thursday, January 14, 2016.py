"""

Ports: uniquely identify a particular program on a particular machine
* programs "bind" to ports (i.e., they say " want to se this port")
   - web servers tend to bind to port 80
* only one program is ever bound to the same port

    ports are numbers in the range 0-65535 (port numbers are 16 bits)


When 2 programs connect  via the Internet, each plays a role.
Sometimes it's strict...
* One program initiates the conversation - "Clients"
* One program accepts the conversation  - "servers"
"""
import socket
import encodings
echo_socket = socket.socket()
echo_socket.connect(('woodhouse.ics.uci.edu', 5151))
text_to_send = "Hello there!\r\n"
text_bytes = text_to_send.encode(encoding= "utf-8")
print(text_bytes)