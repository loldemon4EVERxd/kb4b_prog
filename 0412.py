import matplotlib.pyplot as plt
from menu import clear_console, display, exit, login

def main_menu():
        while True:
            clear_console()
            options = ["stats", "winners", "play", "exit"]
            display(options)
            print()
            choice = input(">: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(options):
                    if options[choice - 1] == "stats":
                        pass
                    elif options[choice - 1] == "winners":
                        pass
                    elif options[choice - 1] == "play":
                        pass
                    elif options[choice - 1] == "exit":
                        exit()
            clear_console()

login()
main_menu()