# polling.py
#
# An implementation of the Polling protocol
import socket
from collections import namedtuple


PollingConnection = namedtuple(
    "PollingConnection",
    ["socket", "input", "output"])

def connect(host: "str", port: 'int'):
    polling_socket = socket.socket()
    polling_socket.connect((host, port))

    polling_input = polling_socket.makefile("r")
    polling_output = polling_socket.makefile("w")

    return PollingConnection(
        socket = polling_socket,
        input = polling_input,
        output = polling_output)


def close(connection: PollingConnection) -> None:
    connection.input.close()
    connection.output.close()
    connection.socket.close()
