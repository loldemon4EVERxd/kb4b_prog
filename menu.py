import os, csv
from time import gmtime, strftime, sleep

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(name):
    for i in range(1, len(name)+1):
        print(f"{i}. {name[i-1]}")

def auth():
    while True:
        clear_console()
        options = ["login", "create new account", "exit"]
        display(options)
        print()
        choice = input(">: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                if options[choice - 1] == "login":
                    with open("0412w/credentials.csv", "r", encoding="utf-8") as nothingvaluable:
                        reader = csv.reader(nothingvaluable, delimiter=';')
                        clear_console()
                        print("*Login*")
                        for i in range(3):
                            username = input("username: ")
                            password = input("password: ")
                            for line in reader:
                                if line[2] == password and line[1] == username:
                                    print("login successful")
                                    sleep(1.0)
                                    return
                            print("wrong username or password, try again")
                        print("too many failed attempts, returning to main menu")
                        sleep(1.0)

                elif options[choice - 1] == "create new account":
                    with open("0412w/credentials.csv", "a", encoding="utf-8") as nothingvaluable:
                        while True:
                            clear_console()
                            print("*Create your account*")
                            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                            username1 = input("username: ")
                            password1 = input("password: ")
                            clear_console()
                            print("*Re-enter your credentials*")
                            username2 = input("username: ")
                            password2 = input("password: ")
                            if username1 == username2 and password1 == password2:
                                send = f'{timestamp};{username2};{password2}'
                                nothingvaluable.write(f'{send}\n')
                                print("account successfully created")
                                sleep(1.0)
                                break
                            print("username or password dont match, try again")
                            sleep(1.0)

                elif options[choice - 1] == "exit":
                    exit()

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

def exit():
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    quit()