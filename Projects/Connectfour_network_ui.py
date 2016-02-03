import Connectfour_ui
import ICS32CFSP
import connectfour


def _welcome_banner():
    """
    Welcome banner for the user inteface
    """
    print("Welcome to the Connect Four Game Client")
    print("---------------------------------------")


def _server_prompt():
    """
    Prompts the user to input the server name or IP and port
    """
    server_input = input("Please enter a server name or IP: ")

    while True:
        if server_input != "woodhouse.ics.uci.edu":
            print("Invalid Server Name")
            return _server_prompt()
        else:
            return server_input

def _port_prompt():
    """
    Prompt the user to input a port number
    """
    port_input = input("Please enter a port number: ")
    while True:
        if int(port_input) != 4444:
            print("Invalid Port Number")
            return _port_prompt()
        else:
            return int(port_input)

def _ask_for_username() -> str:
    """
    Input a username and make sure username is valid
    """
    while True:
        username = input('Username: ').strip()
        check_space = username.split()
        if username != ' ' and len(username) >= 1 and len(check_space) == 1:
            return username
        else:
            print("Please enter a valid input")



def _game_start(connection: ICS32CFSP.ServerConnection):
    """
    Starts the game with the visual board vs the AI.
    Input a move and the server responds with a move.
    """

def user_interface():
    """
     User interface of the game. Enter username and
    """
    connection = ICS32CFSP.Connect(_server_prompt(),_port_prompt())
    username = _ask_for_username()
    _welcome_banner()
    ICS32CFSP.user_sign_in(connection, username)
    ICS32CFSP.AI_request(connection)
    GameState = connectfour.new_game()
    BoardState = Connectfour_ui.game_board(GameState)
    while True:
        ICS32CFSP.server_commands(connection,input("Where do you wanna drop: "))










if __name__ == "__main__":
    user_interface()