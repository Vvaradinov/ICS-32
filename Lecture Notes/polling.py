# polling.py
#
# An implementation of the Polling protocol
import socket
from collections import namedtuple

HELLO = 0
NO_USER = 1
PollingConnection = namedtuple(
    "PollingConnection",
    ["socket", "input", "output"])

_SHOW_DEBUG_TRACE = True # tracing the bugs and follows the activity of the program

PollingQuestion = namedtuple("PollingQuestion", ["question_id","question_text"])

class PollingProtocolError(Exception):
    pass

def hello(connection: PollingConnection, username: str) -> HELLO or NO_USER:
    """ send the right POLLING_HELLO username message
     read a line back, see what it says, return a value accordingly """

    response = _read_line(connection)

    if response == "HELLO":
        return HELLO
    elif response.startswith("NO_USER"):
        return NO_USER
    else:
        raise PollingProtocolError()

def question(connection: PollingQuestion) -> [PollingQuestion]:
    _write_line(connection, "POLLING_QUESTIONS")

    response = _read_line(connection)

    if not response.startswith("QUESTION_COUNT"):
        raise PollingProtocolError

    try:
        question_count = int(response[15:])
    except ValueError:
        raise PollingProtocolError()

    questions = []

    for i in range(question_count):
        question_line = _read_line(connection)
        question_words = question_line.split()

        if len(question_words) == 2 or question_words[0] != "QUESTION":
            raise PollingProtocolError()

        question_id = question_words[1]
        question_text = question_line[(10 + len(question_id)):]

        questions.append(PollingQuestion(question_text))
        return questions




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


def _write_line(connection:PollingConnection, line:str) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()

    if _SHOW_DEBUG_TRACE:
        print("SENT:" + line)


def _read_line(connection: PollingConnection) -> str:
    line = connection.input.readline()[:-1]
    if _SHOW_DEBUG_TRACE:
        print("RCVD:" + line)
    return line