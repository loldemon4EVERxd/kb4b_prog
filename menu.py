import os
from time import gmtime, strftime, time

def login():
    while True:
        clear_console()
        options = ["login", "create new account"]
        display(options)
        print()
        choice = input(">: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                if options[choice - 1] == "login":
                    with open("0412w/credentials.csv", "r", encoding="utf-8") as nothingvaluable:
                        clear_console()
                        print("*Login*")
                        for i in range(3):
                            username = input("username: ")
                            password = input("password: ")
                            if username in nothingvaluable.read() and password in nothingvaluable.read():
                                break
                            print("wrong username or password, try again")
                        print("too many failed attempts, returning to main menu")
                elif options[choice - 1] == "create new account":
                    with open("0412w/credentials.csv", "a", encoding="utf-8") as nothingvaluable:
                        clear_console()
                        print("*Create your account*")
                        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        username = input("username: ")
                        password = input("password: ")
                        send = f'{timestamp};{username};{password}'
                        nothingvaluable.write(f'{send}\n')
                elif options[choice - 1] == "exit":
                    exit()

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(name):
    for i in range(1, len(name)+1):
        print(f"{i}. {name[i-1]}")

def exit():
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    quit()

def main_menu():
        while True:
            clear_console()
            options = ["would"]
            options += ["smash", "or", "exit"]
            display(options)
            print()
            choice = input(">: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(options):
                    if options[choice - 1] == "would":
                        pass
                    elif options[choice - 1] == "smash":
                        pass
                    elif options[choice - 1] == "or":
                        pass
                    elif options[choice - 1] == "exit":
                        exit()
            clear_console()