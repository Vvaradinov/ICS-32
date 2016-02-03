import socket
from collections import namedtuple

CONNECTFOUR_HOST = 'woodhouse.ics.uci.edu'
CONNECTFOUR_PORT = 4444

ServerConnection = namedtuple("ServerConnection", ["socket", "input","output"])
ServerResponse = namedtuple("ServerResponse", ["response","col_num"])

class ServerError(Exception):
    pass


def Connect(host: str, port: int) -> ServerConnection:
    """
    Connects to the server on the given host and port number, returns an updated ServerConnection namedtuple
    """
    server_socket = socket.socket()
    server_socket.connect((host, port))

    server_input = server_socket.makefile("r")
    server_output = server_socket.makefile("w")

    return ServerConnection(socket = server_socket, input = server_input, output = server_output)



def user_sign_in(connection: ServerConnection, user_name: str) -> None:
    """
    User login prompt in order to proceed with the game
    """




def _write_line(connection: ServerConnection, line: str) -> None:
    '''
    Writes a line of text to the server and ends with a new line
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()

def _read_line(connection: ServerConnection) -> str:
    '''
    Reads a line of text sent from the server
    '''
    return connection.input.readline()[:-1]


def _outcome_(connection: ServerConnection, outcome: str) -> None:
    '''
    Reads line sent from the server, outcome should have a particular form
    If unexpected outcome, then
    function raises an exception.
    '''
    line = _read_line(connection)

    if line != outcome:
        print(line)
        raise ServerError()
