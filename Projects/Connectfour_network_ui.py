# Vladislav Varadinov  32979197 #Linxuan Xin 11311415
import Connectfour_ui
import ICS32CFSP
import connectfour
import common_functions


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
    game_state = connectfour.new_game()
    common_functions.game_board(game_state)
    while True:
        game_state, message = common_functions.make_choice(game_state, common_functions.drop_or_pop(), common_functions.col_num())
        AI_message = ICS32CFSP.server_commands(connection, message)
        if type(AI_message) == tuple:
            game_state = common_functions.get_state(AI_message, game_state)
            common_functions.game_board(game_state)
        elif AI_message == 'Player wins!':
            print('-------------------------Final State---------------------------')
            common_functions.game_board(game_state)
            print('\r\nPlayer wins!\nGame Over. Congratulation!')
        else:
            try:
                game_state = common_functions.get_state(AI_message, game_state)
            except:
                print('Connection Error.')

        print('-------------------------New State----------------------------')
        common_functions.game_board(game_state)


def user_interface():
    """
     User interface of the game.
    """
    while True:
        print('This is ConnectFour Game!' )
        connection = ICS32CFSP.Connect(_server_prompt(), _port_prompt())
        username = _ask_for_username()
        ICS32CFSP.user_sign_in(connection, username)
        ICS32CFSP.AI_request(connection)
        _game_start(connection)




if __name__ == "__main__":
    user_interface()