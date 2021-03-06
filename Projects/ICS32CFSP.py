# Vladislav Varadinov  32979197 #Linxuan Xin 11311415
import socket
from collections import namedtuple
import connectfour
import Connectfour_ui

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
    _write_line(connection, "I32CFSP_HELLO" + " " + user_name)
    _outcome_(connection, "WELCOME" + " " + user_name)


def AI_request(connection: ServerConnection) -> None:
    """
    Requests a game to start with an artificial intelligence
    After the AI is ready it will say "READY"
    """
    _write_line(connection, "AI_GAME")
    _outcome_(connection, "READY")


def server_commands(connection: ServerConnection, player_commands: str):
    """
    Sends the server our commands and responds with the commands of the AI
    If the action is invalid it will re-prompt the user
    """
    start_line = player_commands.strip().upper()
    start_word = player_commands.split()
    _write_line(connection,start_line)
    check = _read_line(connection)

    if check == "OKAY":
        ai_response_line = _ai_outcome(connection)
        if ai_response_line == ["WINNER_RED"]:
            return "Player Wins"
        ai_answer = ai_response_line[0]
        ai_colum = int(ai_response_line[1]) - 1
        print("AI: " + ai_answer + " " + str(ai_colum + 1) )
        done = _read_line(connection)

        if done == "READY":
            return ServerResponse(response = ai_answer, col_num =  ai_colum)

        if done == 'WINNER_YELLOW':
            return ('AI wins!', ServerResponse(response = ai_answer, col_num = ai_colum))

        else:
            _outcome_(connection, "READY")
            print("Invalid input.")


def _ai_outcome(connection: ServerConnection):
    return _read_line(connection).split()


def close_server(connection: ServerConnection) -> None:
    """
    Closing server connection
    """
    connection.socket.close()
    connection.input.close()
    connection.output.close()


def _write_line(connection: ServerConnection, line: str) -> None:
    """
    Writes a line of text to the server and ends with a new line
    """
    connection.output.write(line + '\r\n')
    connection.output.flush()

def _read_line(connection: ServerConnection) -> str:
    """
    Reads a line of text sent from the server
    """
    return connection.input.readline()[:-1]


def _outcome_(connection: ServerConnection, outcome: str) -> None:
    """
    Reads line sent from the server, outcome should have a particular form
    If unexpected outcome, then
    function raises an exception.
    """
    line = _read_line(connection)

    if line != outcome:
        print(line)
        raise ServerError()

