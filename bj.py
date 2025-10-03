import os
import time
import random

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(name):
    for i in range(1, len(name)+1):
        print(f"{i}. {name[i-1]}")

NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]
MAX_HAND = 21

class Player:
    def __init__(self, chips):
        self.chips = chips
        self.cards = []

    def hand_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card[:-1] == "A":
                aces += 1
                value += 11
            elif card[:-1] in ["K", "Q", "J"]:
                value += 10
            else:
                value += int(card[:-1])
        while value > MAX_HAND and aces > 0:
            value -= 10
            aces -= 1
        return value
    
class Dealer:
    def __init__(self):
        self.cards = []

    def hand_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card[:-1] == "A":
                aces += 1
                value += 11
            elif card[:-1] in ["K", "Q", "J"]:
                value += 10
            else:
                value += int(card[:-1])
        while value > MAX_HAND and aces > 0:
            value -= 10
            aces -= 1
        return value

class Menu:
    def main_menu(self):
            clear_console()
            if P1.chips <= 0:
                print("DEFEAT (u broke lmao)")
                time.sleep(2)
                quit()
            while True:
                options = ["BONUSMAXWINSCATTERGOGOGO", "ur chips", "exit"]
                display(options)
                print()
                choice = input(">: ")
                clear_console()
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(options):
                        if options[choice - 1] == "BONUSMAXWINSCATTERGOGOGO":
                            self.bet()
                            self.pregame()
                            quit()
                        elif options[choice - 1] == "ur chips":
                            clear_console()
                            print(f"YOU HAVE {P1.chips} CHIPS")
                            print()
                            time.sleep(1)
                            input("""type 𝐞⃥⃒̸ꞆᎽ𝐫⃥⃒̸ʜƚ𝔦𝔠y҉𝔯Ĭꕷᙁi҉ᴥᴄᴥᴛᴥ to exit
                                        >: """)
                            clear_console()
                        elif options[choice - 1] == "exit":
                            print("nuking the game...") 
                            quit()

    def bet(self):
        self.bet_amount = 0
        while True:
            clear_console()
            print(f"YOU HAVE {P1.chips} CHIPS")
            self.bet_amount = input("Enter your bet amount: ")
            if self.bet_amount.isdigit():
                self.bet_amount = int(self.bet_amount)
                if 0 < self.bet_amount <= P1.chips:
                    P1.chips -= self.bet_amount
                    print(f"You've bet {self.bet_amount} chips.")
                    break
                elif self.bet_amount > P1.chips:
                    print("brokie")
                    time.sleep(1)

    def gen_card(self):
        r_num = random.choice(NUMS)
        r_suit = random.choice(SUITS)
        r_card = f"{r_num}{r_suit}"
        return r_card

    def pregame(self):
        Pablo.cards.append(self.gen_card())
        P1.cards.append(self.gen_card())
        P1.cards.append(self.gen_card())
        self.game()

    def player_deal(self):
        P1.cards.append(self.gen_card())

    def game(self):
        while True:
            clear_console()
            print(f"PABLO'S HAND: {' '.join(Pablo.cards)} XX")
            print(f"YOUR HAND: {' '.join(P1.cards)}")
            if P1.hand_value() > MAX_HAND:
                print("BUSTTTTTT")
                time.sleep(1)
                self.reset()
            choice = input("HIT? >: ")
            if choice in ["yes", "y", "YES"]:
                self.player_deal()
                if P1.hand_value() == MAX_HAND:
                    print("BJ!")
                    self.final_destination()
            elif choice in ["no", "n", "NO"]:
                self.final_destination()
                break

    def final_destination(self):
        while Pablo.hand_value() < 17:
            clear_console()
            Pablo.cards.append(self.gen_card())
            print(f"PABLO'S HAND: {' '.join(Pablo.cards)}")
            print(f"YOUR HAND: {' '.join(P1.cards)}")
            input("...press smth ok plz >: ")
        pablo_hand = Pablo.hand_value()
        player_hand = P1.hand_value()
        if pablo_hand > MAX_HAND:
            print("PABLO BUSTED! YOU WIN! XDXDX")
            P1.chips += 2 * self.bet_amount
        elif player_hand > pablo_hand:
            print("YOU WIN! XDXDX")
            P1.chips += 2 * self.bet_amount
        elif player_hand < pablo_hand:
            print("PABLO WINS! XDXDX")
        else:
            print("draw")
            P1.chips += self.bet_amount
        self.reset()

    def reset(self):
        P1.cards.clear()
        Pablo.cards.clear()
        print()
        input("again? :3")
        self.main_menu()

P1 = Player(500)
Pablo = Dealer()


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()