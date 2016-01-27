import polling

POLLING_HOST = "woodhouse.ics.uci.edu"
POLLING_PORT = 5501

def show_welcome_banner() -> None:
    print("Welcome to the Polling client")
    print()


def ask_for_username() -> str:
    while True:
        username = input("Username: ").strip()

        if len(username) > 0:
            return username
        else:
            print("That is not a valid username; please try again")



def login_with_valid_username(connection: polling.PollingConnection) -> None:
    while True:
        username = ask_for_username()

        hello_result = polling.hello(connection, username)

        if hello_result == polling.HELLO:
            return username
        else:
            print("That's not a valid username; please try again")


def handle_command(connection: polling.PollingConnection) -> bool:
    command = input("[V]ote, [R]esult or [G]oodbye").strip().upper()

    if command.startswith("V"):
        handle_vote_command(connection)
        return True
    elif command.startswith("R"):
        handle_results_command(connection)
        return True
    elif command.startswith("G"):
        handle_goodbye_command(connection)
        return False
    else:
        print("That is not a valid command")
        return True



def handle_vote_command(connection: polling.PollingConnection) -> None:
    print("Not yet implemented")

def handle_results_command(connection: polling.PollingConnection)-> None:
    print("Not yet implemented")

def handle_goodbye_command(connection: polling.PollingConnection) -> None:
    print("Goodbye")




def run_user_interface() -> None:
    show_welcome_banner()

    connection = polling.connect(POLLING_HOST, POLLING_PORT)

    try:
        username = login_with_valid_username(connection)

        while handle_command(connection):
            pass

    finally:
        polling.close(connection)

    print("We are out of here")


if __name__ == "__main__":
    run_user_interface()