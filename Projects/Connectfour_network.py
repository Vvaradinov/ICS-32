import Connectfour_ui


def welcome_banner():
    """
    Welcome banner for the user inteface
    """
    print("Welcome to the Connect Four Game Client")
    print("---------------------------------------")

def ask_for_username()-> str:
    """
    Prompts the user to enter his username
    """
    while True:
        username = input("Username: ").strip()

        if len(username) > 0:
            print("Hello", username)
            return username
        else:
            print("That is not a valid username, please try again")


def login_with_valid_username(connection: polling.PollingConnection) -> None:
    while True:
        username = ask_for_username()

        hello_result = polling.hello(connection, username)

        if hello_result == polling.HELLO:
            return username
        else:
            print("That's not a valid username; please try again")




if __name__ == "__main__":
    ask_for_username()