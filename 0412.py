import os
import matplotlib.pyplot as plt
from time import gmtime, strftime, sleep
import csv
import random

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(name):
    for i in range(1, len(name)+1):
        print(f"{i}. {name[i-1]}")

def exitx():
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    quit()

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
                        for i in range(3):
                            with open("0412w/credentials.csv", "r", encoding="utf-8") as nothingvaluable:
                                reader = csv.reader(nothingvaluable, delimiter=';')
                                clear_console()
                                print("*Login*")
                                username = input("username: ")
                                password = input("password: ")
                                for line in reader:
                                    if line[2] == password and line[1] == username:
                                        print("login successful")
                                        global CURRLOG
                                        CURRLOG = username
                                        sleep(1.0)
                                        return
                            print("wrong username or password, try again")
                            sleep(1.0)
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
                    exitx()

def main_menu():
        gamestart = True
        yech = ["yes", "YES", "y", "Y", "1", "true", "True", "TRUE"]
        noch = ["no", "NO", "n", "N", "0", "false", "False", "FALSE"]
        while True:
            clear_console()
            options = ["stats", "winners", "wanna be a millionaire?", "exit"]
            display(options)
            print()
            choice = input(">: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(options):
                    if options[choice - 1] == "stats":
                        easyc = 0
                        medc = 0
                        hardc = 0
                        with open("2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv", "r", encoding="utf-8") as q:
                            reader = csv.reader(q, delimiter=';')
                            for line in reader:
                                if line[1] == "easy":
                                    easyc += 1
                                elif line[1] == "medium":
                                    medc += 1
                                elif line[1] == "hard":
                                    hardc += 1
                        plt.bar(["easy", "medium", "hard"], [easyc, medc, hardc])
                        plt.title("category ratio in dataset *questions*")
                        plt.ylabel("question count")
                        plt.xticks(rotation=45, ha="right")
                        plt.tight_layout()
                        plt.show()

                    elif options[choice - 1] == "winners":
                        with open("0412w/winners.csv", "r", encoding="utf-8") as w:
                            reader = csv.reader(w, delimiter=';')
                            clear_console()
                            print("*Winner List*")
                            for line in reader:
                                print(f'{line[1]} at {line[0]} left a message: "{line[2]}"')
                            input(">: ")
                                


                    elif options[choice - 1] == "wanna be a millionaire?":
                        easy = []
                        med = []
                        hard = []
                        with open("2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv", "r", encoding="utf-8") as q:
                            reader = csv.reader(q, delimiter=',')
                            for line in reader:
                                if line[1] == "easy":
                                    easy.append({"q": line[3], "ansr": line[4]})
                                elif line[1] == "medium":
                                    med.append({"q": line[3], "ansr": line[4]})
                                elif line[1] == "hard":
                                    hard.append({"q": line[3], "ansr": line[4]})
                            clear_console()
                            print("do u wanna be rich")
                            while gamestart == True:
                                clear_console()
                                print("do u wanna be rich?")
                                answr = input(">: ")
                                if answr in noch:
                                    sleep(1.0)
                                    print("ok, fk u then")
                                    exitx()
                                elif answr in yech:
                                    while gamestart == True:
                                        clear_console()
                                        print("r u sure?")
                                        answr = input(">: ")
                                        if answr in noch:
                                            sleep(1.0)
                                            print("ok, fk u then")
                                            exitx()
                                        elif answr in yech:
                                            while gamestart == True:
                                                clear_console()
                                                print("so you dont want to continue?")
                                                answr = input(">: ")
                                                if answr in yech:
                                                    sleep(4)
                                                    print("gp q urself")
                                                    sleep(1)
                                                elif answr in noch:
                                                    sleep(1)
                                                    print("LET'S GET RICH THEN")
                                                    sleep(1)
                                                    print("glhf, you'll need it")
                                                    sleep(1)
                                                else:
                                                    continue
                                                gamestart = False
                            for i in range(4):
                                clear_console()
                                r = random.choice(easy)
                                print(f"round {i+1} - ez:")
                                print(r["q"])
                                lckin = input(">: ")
                                if r["ansr"] == "True":
                                    if lckin in yech:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                                else:
                                    if lckin in noch:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                            for i in range(4):
                                clear_console()
                                r = random.choice(med)
                                print(f"round {i+5} - mid:")
                                print(r["q"])
                                lckin = input(">: ")
                                if r["ansr"] == "True":
                                    if lckin in yech:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                                else:
                                    if lckin in noch:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                            for i in range(4):
                                clear_console()
                                r = random.choice(hard)
                                print(f"round {i+9} - hard:")
                                print(r["q"])
                                lckin = input(">: ")
                                if r["ansr"] == "True":
                                    if lckin in yech:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                                else:
                                    if lckin in noch:
                                        print("ts was right yn")
                                        sleep(1)
                                    else:
                                        print("eternal damnation, what a shame")
                                        exitx()
                        sleep(2)
                        clear_console()
                        print("CONGRATS, U RICH NOW")
                        themsg = input("leave a msg for the other yns: ")
                        with open("0412w/winners.csv", "a", encoding="utf-8") as q:
                            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                            send = f'{timestamp};{CURRLOG};{themsg}'
                            q.write(f'{send}\n')

                    elif options[choice - 1] == "exit":
                        exitx()

auth()
main_menu()