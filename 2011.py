import random
from time import gmtime, strftime
import os
import random
import time

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(name):
    for i in range(1, len(name)+1):
        print(f"{i}. {name[i-1]}")

def generator():
    min = int(input('min: '))
    max = int(input('max: '))
    n = int(input('count: '))
    with open("2011w/zapis.txt", "w", encoding="utf-8") as file:
        for i in range(n):
            gen = random.randint(min, max)
            file.write(f'{str(gen)}\n')

def chatlog():
    print('Type "exit" to quit.')
    with open("2011w/chatlog.txt", "w", encoding="utf-8") as file:
        while True:
            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            nick = input('nickname: ')
            message = input('message: ')
            if message.lower() == 'exit':
                break
            send = f'{timestamp} {nick}: {message}'
            file.write(f'{send}\n')

def betano():
    user_logged = False
    while True:
        options = ["create account", "login", "bet"]
        display(options)
        choice = input(">: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                if choice == 1:
                    clear_console()
                    nick = input('nickname: ')
                    password = input('password: ')
                    blue_essence = 1000
                    with open("2011w/betano_accounts.txt", "a", encoding="utf-8") as file:
                        file.write(f'{nick};{password};{blue_essence}\n')
                elif choice == 2:
                    clear_console()
                    if nick is None:
                        print('no account found, please create one first')
                        continue
                    login_nick = input('nickname: ')
                    login_password = input('password: ')
                    if login_nick == nick and login_password == password:
                        print(f'you have {blue_essence} blue essence left')
                        user_logged = True
                    else:
                        print('login failed')
                elif choice == 3:
                    if user_logged == False:
                        print('please login first')
                        continue
                    else:
                        cointoss = random.choice(['heads', 'tails'])
                        user_bet = input('heads or tails: ')
                        amount = int(input('amount to bet: '))
                        if cointoss == user_bet:
                            blue_essence += amount
                            print(f'you won {amount} blue essence')
                        else:
                            blue_essence -= amount
                            print(f'loser')

# generator()
# chatlog()
betano()