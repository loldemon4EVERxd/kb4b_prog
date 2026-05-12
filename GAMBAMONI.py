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

def displaymons(name):
    for i in range(1, len(name)-5):
        print(f"{i}. {name[i-1]}")

ALLMONS = []
ALLMONSNAMESONLY = []
ALLTRAINERS = []
ALLTRAINERSNAMESONLY = []

class Cichnamon:
    def __init__(self, name, level, hp, power):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.power = power
        ALLMONS.append(self)
        ALLMONSNAMESONLY.append(self.name)

    def info(self):
        print(f"{self.name}, lvl({self.level}) - {self.hp}hp, {self.power}str")
        print("---------------------------------------------")

    def reset_hp(self):
        self.hp = self.max_hp

class Trainer:
    def __init__(self, name, wins, loses):
        self.name = name
        self.wins = wins
        self.loses = loses
        self.collection = []
        ALLTRAINERS.append(self)
        ALLTRAINERSNAMESONLY.append(self.name)

    def collect(self, cichnamon):
        self.collection.append(cichnamon)

    def discard(self, cichnamon):
        self.collection.remove(cichnamon)

    def winrate(self):
        total = self.wins + self.loses
        if total == 0:
            return "N/A (no matches played)"
        elif self.wins > 0 and self.loses == 0:
            return "100%"
        else:
            return f"{self.wins / total * 100:.2f}%"

    def info(self): # po dokonceni setupu se aktualizujou cichnamoni v collection u treneru
        print(f"""  {self.name}
   wins: {self.wins}
  loses: {self.loses}
 winrate: {self.winrate()}""")
        print("collection: ", end=" ")
        for cichnamon in self.collection:
           print(cichnamon.name, end=", ")
        print()
        print("--------------------------------------")

class Menu:
    def __init__(self):
        self.setup_done = False
        self.next_setup_done = True
        self.round_counter = 1
        ALLMONS.remove(Igris)
        ALLMONS.remove(Ant_King)
        ALLMONS.remove(Deer3)
        ALLMONS.remove(Deer4)
        ALLMONS.remove(Deer5)
        ALLMONS.remove(Deer6)

    def main_menu(self):
        clear_console()
        while True:
            options = ["ultimate bravery"]
            if not self.setup_done:
                options.append("setup")
            if not self.next_setup_done:
                options.append("next_setup")
            options += ["trainers", "remaining cichnamons", "exit"]
            display(options)
            print()
            choice = input(">: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(options):
                    if options[choice - 1] == "ultimate bravery":
                        if not self.setup_done or not self.next_setup_done:
                            print("⚠️ !!! COMPLETE SETUP FIRST !!! ⚠️")
                            time.sleep(1.2)
                            clear_console()
                        else:
                            clear_console()
                            self.ultimate_bravery()
                    elif options[choice - 1] == "setup": # nejdriv se musi udelat setup, pak se zapne a odemkne se fight (ultimate bravery)
                        clear_console()
                        self.trainer_choose()
                    elif options[choice - 1] == "next_setup": # hraje se na 3 kola a pokazde se udela znova setup s jinyma cichnamona (ti kteri nebyli predtim pouziti)
                        clear_console()
                        self.next_setup_done = True
                        self.cichnamon_choose()
                    elif options[choice - 1] == "trainers":
                        clear_console()
                        print("--------------------------------------")
                        SungJinwoo.info()
                        Nokotan.info()
                        Trebuchet.info()
                        print()
                        input("""type 𝐞⃥⃒̸ꞆᎽ𝐫⃥⃒̸ʜƚ𝔦𝔠y҉𝔯Ĭꕷᙁi҉ᴥᴄᴥᴛᴥ to exit
                                        >: """)
                    elif options[choice - 1] == "remaining cichnamons":
                        clear_console()
                        print("---------------------------------------------")
                        for cichnamon in ALLMONS:
                            cichnamon.info()
                        print()
                        input("""type 𝐞⃥⃒̸ꞆᎽ𝐫⃥⃒̸ʜƚ𝔦𝔠y҉𝔯Ĭꕷᙁi҉ᴥᴄᴥᴛᴥ to exit
                                        >: """)
                    elif options[choice - 1] == "exit":
                        print("nuking the game...") 
                        quit()
            clear_console()

    def trainer_choose(self): # kazdy hrac si vybere trenera kterej ma nejakou specialni abilitu
        P1 = input("P1, inscribe ur esteemed name: ")
        clear_console()
        P2 = input("P2, inscribe ur esteemed name: ")
        time.sleep(0.8)
        clear_console()
        self.first_player = random.choice([P1, P2]) # na random se zvoli kdo bude vybirat jako prvni
        self.second_player = P2 if self.first_player == P1 else P1
        print(f"{self.first_player} shall proceed first")
        time.sleep(1.5)
        clear_console()
        available_trainers = ALLTRAINERS[:]
        available_trainers_names = ALLTRAINERSNAMESONLY[:]
        while True:
            print(f"{self.first_player}, select ur trainer:")
            display(available_trainers_names)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(available_trainers):
                    self.first_trainer = available_trainers.pop(i)
                    self.first_trainer_name = available_trainers_names.pop(i)
                    clear_console()
                    break
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()

        while True:
            print(f"{self.second_player}, select ur trainer:")
            display(available_trainers_names)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(available_trainers):
                    self.second_trainer = available_trainers.pop(i)
                    self.second_trainer_name = available_trainers_names.pop(i)
                    clear_console()
                    print(f"{self.first_player} selected {self.first_trainer_name}")
                    print(f"{self.second_player} selected {self.second_trainer_name}")
                    print()
                    input("type Æ to continue...")
                    time.sleep(0.2)
                    clear_console()
                    self.cichnamon_choose()
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()

    def cichnamon_choose(self): # oba maji main a backup cichnamona pokud by ten prvni zemrel
        while True:
            print(f"{self.first_player}, choose ur main cichnamon:")
            displaymons(ALLMONSNAMESONLY)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(ALLMONS):
                    self.first_mon = ALLMONS.pop(i)
                    self.first_mon_name = ALLMONSNAMESONLY.pop(i)
                    time.sleep(0.2)
                    self.first_trainer.collect(self.first_mon)
                    clear_console()
                    break
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()

        while True:
            print(f"{self.second_player}, choose ur main cichnamon:")
            displaymons(ALLMONSNAMESONLY)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(ALLMONS):
                    self.second_mon = ALLMONS.pop(i)
                    self.second_mon_name = ALLMONSNAMESONLY.pop(i)
                    time.sleep(0.2)
                    clear_console()
                    self.second_trainer.collect(self.second_mon)
                    print(f"{self.first_player} selected {self.first_mon.name}")
                    print(f"{self.second_player} selected {self.second_mon.name}")
                    print()
                    input("type Æ to continue...")
                    time.sleep(0.2)
                    clear_console()
                    break
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()

        while True:
            print(f"{self.first_player}, choose ur backup cichnamon:")
            displaymons(ALLMONSNAMESONLY)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(ALLMONS):
                    self.backup_mon = ALLMONS.pop(i)
                    self.backup_mon_name = ALLMONSNAMESONLY.pop(i)
                    time.sleep(0.2)
                    self.first_trainer.collect(self.backup_mon)
                    clear_console()
                    break
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()

        while True:
            print(f"{self.second_player}, choose ur backup cichnamon:")
            displaymons(ALLMONSNAMESONLY)
            print()
            choice = input(">: ")
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(ALLMONS):
                    self.backup_mon2 = ALLMONS.pop(i)
                    self.backup_mon2_name = ALLMONSNAMESONLY.pop(i)
                    time.sleep(0.2)
                    clear_console()
                    self.second_trainer.collect(self.backup_mon2)
                    print(f"{self.first_player} selected {self.first_mon.name}, {self.backup_mon.name}")
                    print(f"{self.second_player} selected {self.second_mon.name}, {self.backup_mon2.name}")
                    print()
                    input("type Æ to continue...")
                    time.sleep(0.2)
                    clear_console()
                    break
            print("an unrecognized choice, please endeavor once more")
            time.sleep(0.6)
            clear_console()
        self.setup_done = True
        self.main_menu()

    def ultimate_bravery(self):
        round_counter = 1
        print("------the brawl shall now begin------")
        print(f"***{self.first_player}***")
        time.sleep(0.5)
        print(f"TRAINER: {self.first_trainer_name}")
        time.sleep(0.5)
        print(f"MAIN CICHNAMON: {self.first_mon_name}")
        time.sleep(0.5)
        print(f"BACKUP CICHNAMON: {self.backup_mon_name}")
        print()
        input("type Æ to continue...")
        time.sleep(0.2)
        clear_console()
        print("------please rate 5 stars on google store------")
        print(f"***{self.second_player}***")
        time.sleep(0.5)
        print(f"TRAINER: {self.second_trainer_name}")
        time.sleep(0.5)
        print(f"MAIN CICHNAMON: {self.second_mon_name}")
        time.sleep(0.5)
        print(f"BACKUP CICHNAMON: {self.backup_mon2_name}")
        print()
        input("type Æ to continue...")
        time.sleep(0.2)
        clear_console()

        print("---------------------------------------------")
        print(f"ROUND {self.round_counter} HAS NOW BEGUN")
        input("---------------------------------------------")
        ARISE = random.random() # sung replacne zvolene cichnamony ant kingem a igrisem (sololeveling)
        if ARISE < 0.2 and SungJinwoo in (self.first_trainer, self.second_trainer):
            if SungJinwoo == self.first_trainer:
                self.first_trainer.discard(self.first_mon)
                self.first_trainer.discard(self.backup_mon)
                self.first_trainer.collect(Igris)
                self.first_trainer.collect(Ant_King)
                self.first_mon = Igris
                self.backup_mon = Ant_King
            else:
                self.second_trainer.discard(self.second_mon)
                self.second_trainer.discard(self.backup_mon2)
                self.second_trainer.collect(Igris)
                self.second_trainer.collect(Ant_King)
                self.second_mon = Igris
                self.backup_mon2 = Ant_King
            print("SungJinwoo used his skill *ARISE*, Igris and Ant King have been summoned")
            input("---------------------------------------------")

        player1_mons = [self.first_mon, self.backup_mon]
        player2_mons = [self.second_mon, self.backup_mon2]
        current1 = player1_mons.pop(0)
        current2 = player2_mons.pop(0)

        DEER_ARMY = random.random() # nokotan si summonne dasi 4 jeleny na pomoc
        if DEER_ARMY < 0.2 and Nokotan in (self.first_trainer, self.second_trainer):
            Nokotan.collect(Deer3)
            Nokotan.collect(Deer4)
            Nokotan.collect(Deer5)
            Nokotan.collect(Deer6)
            if Nokotan == self.first_trainer:
                player1_mons.append(Deer3)
                player1_mons.append(Deer4)
                player1_mons.append(Deer5)
                player1_mons.append(Deer6)
            else:
                player2_mons.append(Deer3)
                player2_mons.append(Deer4)
                player2_mons.append(Deer5)
                player2_mons.append(Deer6)
            print("Nokotan used her skill *DEER ARMY*, DEER POWER!")
            input("---------------------------------------------")

        while True:
            attacker = random.choice([self.first_player, self.second_player]) # na random se zvoli kdo bude fightit jako prvni
            defender = self.second_player if attacker == self.first_player else self.first_player
            attacker_mon = current1 if attacker == self.first_player else current2
            defender_mon = current2 if attacker == self.first_player else current1
            ARTILLERY= random.random() # kazdy tah ma trebuchet 10% sanci na instakill enemy cichnamona pokud je attacker
            if ARTILLERY < 0.1 and Trebuchet in (self.first_trainer, self.second_trainer):
                if Trebuchet == self.first_trainer and attacker == self.first_player:
                    defender_mon.hp = 0
                    print(f"Trebuchet's skill *ARTILLERY* has been actived, massive rock incoming")
                    input("---------------------------------------------")
                elif Trebuchet == self.second_trainer and attacker == self.second_player:
                    defender_mon.hp = 0
                    print(f"Trebuchet's skill *ARTILLERY* has been actived, massive rock incoming")
                    input("- - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print(f"{attacker}'s \033[1m{attacker_mon.name}\033[0m is attacking {defender}'s \033[1m{defender_mon.name}\033[0m")
                input("- - - - - - - - - - - - - - - - - - - - - - -")
                action = random.random()
                if 0.08 <= action < 0.15:
                    print(f"\033[1m{attacker_mon.name}\033[0m onetapped \033[1m{defender_mon.name}\033[0m with a special attack")
                    input("- - - - - - - - - - - - - - - - - - - - - - -")
                    defender_mon.hp = 0
                elif action < 0.08:
                    print(f"\033[1m{attacker_mon.name}\033[0m had a stroke")
                    input("- - - - - - - - - - - - - - - - - - - - - - -")
                    attacker_mon.hp = 0
                else:
                    print(f"\033[1m{attacker_mon.name}\033[0m deals {attacker_mon.power} damage")
                    last_hp = defender_mon.hp
                    defender_mon.hp -= attacker_mon.power
                    print(f"\033[1m{defender_mon.name}\033[0m, {last_hp}hp => {defender_mon.hp}hp")
                    input("- - - - - - - - - - - - - - - - - - - - - - -")
            HEAL = random.random()
            if HEAL < 0.5 and self.backup_mon == Medic and current1 != Medic:
                if current1.hp < 1:
                    current1.hp = 0
                    current1.hp += 1
                    print(f"\033[1m{current1.name}\033[0m has been revived, current hp => {current1.hp}")
                else:
                    self.first_mon.hp += 147 # MUZE TAM BYT I OVERHEAL
                    print(f"\033[1m{current1.name}\033[0m has been healed, current hp => {current1.hp}")
            if HEAL < 0.5 and self.backup_mon2 == Medic and current2 != Medic:
                if current2.hp < 1:
                    current2.hp = 0
                    current2.hp += 1
                    print(f"\033[1m{current2.name}\033[0m has been revived, current hp => {current2.hp}")
                else:
                    current2.hp += 147
                    print(f"\033[1m{current2.name}\033[0m has been healed, current hp => {current2.hp}")
            if defender_mon.hp <= 0:
                print(f"\033[1m{defender_mon.name}\033[0m has died")
                input("---------------------------------------------")
                if defender == self.first_player:
                    if player1_mons:
                        current1 = player1_mons.pop(0)
                        print(f"{self.first_player} soughts assistance from \033[1m{current1.name}\033[0m")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                    else:
                        print(f"***\033[1m{self.second_player}\033[0m achieves victory!***")
                        input("---------------------------------------------")
                        self.second_trainer.wins += 1
                        self.second_mon.level += 10
                        self.backup_mon2.level += 5
                        self.first_trainer.loses += 1
                        break
                else:
                    if player2_mons:
                        current2 = player2_mons.pop(0)
                        print(f"{self.second_player} soughts assistance from \033[1m{current2.name}\033[0m")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                    else:
                        print(f"***\033[1m{self.first_player}\033[0m achieves victory!***")
                        input("---------------------------------------------")
                        self.first_trainer.wins += 1
                        self.first_mon.level += 10
                        self.backup_mon.level += 5
                        self.second_trainer.loses += 1
                        break

            if attacker_mon.hp <= 0:
                print(f"\033[1m{attacker_mon.name}\033[0m has died")
                input("---------------------------------------------")
                if attacker == self.first_player:
                    if player1_mons:
                        current1 = player1_mons.pop(0)
                        print(f"{self.first_player} soughts assistance from \033[1m{current1.name}\033[0m")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                    else:
                        print(f"***\033[1m{self.second_player}\033[0m achieves victory***")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                        self.second_trainer.wins += 1
                        self.second_mon.level += 10
                        self.backup_mon2.level += 5
                        self.first_trainer.loses += 1
                        break
                else:
                    if player2_mons:
                        current2 = player2_mons.pop(0)
                        print(f"{self.second_player} soughts assistance from \033[1m{current2.name}\033[0m")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                    else:
                        print(f"***\033[1m{self.first_player}\033[0m achieves victory***")
                        input("- - - - - - - - - - - - - - - - - - - - - - -")
                        self.first_trainer.wins += 1
                        self.first_mon.level += 10
                        self.backup_mon.level += 5
                        self.second_trainer.loses += 1
                        break
        self.next_setup_done = False
        self.round_counter += 1
        if self.round_counter == 4:
            clear_console()
            print("ty for playing my game <3")
            print()
            input("type w/e u want to end the game")
            quit()
        
        clear_console()
        print("time to heal up...")
        if DEER_ARMY < 0.2:
            Nokotan.discard(Deer3)
            Nokotan.discard(Deer4)
            Nokotan.discard(Deer5)
            Nokotan.discard(Deer6)
            Deer3.reset_hp()
            Deer4.reset_hp()
            Deer5.reset_hp()
            Deer6.reset_hp()
        if ARISE < 0.2:
            Ant_King.reset_hp()
            Igris.reset_hp()
        time.sleep(1.5)

        print("all ur cichnamons ran away from yall") # cichnamoni se odeberou 
        self.first_trainer.discard(self.first_mon)
        self.second_trainer.discard(self.second_mon)
        self.first_trainer.discard(self.backup_mon)
        self.second_trainer.discard(self.backup_mon2)
        time.sleep(1.5)
        
        print("ready for the next round?")
        time.sleep(2)







Magik = Cichnamon("Magik", 19, 357, 161)
Yennefer = Cichnamon("Yennefer", 94, 90, 501)
Deer = Cichnamon("Deer", 5, 22, 151)
Deer2 = Cichnamon("Deer2", 3, 342, 16)
Ezio = Cichnamon("Ezio", 40, 21, 451)
Kassawin= Cichnamon("Kassawin", 68, 187, 368)
Winston = Cichnamon("Winston", 39, 1, 1)
Arya = Cichnamon("Arya", 11, 1, 185)
Medic = Cichnamon("Medic", 31, 31, 5) # muze healovat a revivovat main cichnamona pokud je backup
Malphite = Cichnamon("Malphite", 3250, 1301, 39)
Trevor = Cichnamon("Trevor", 49, 49, 158)
Assassino_Cappuccino = Cichnamon("Assassino_Cappuccino", 225, 71, 71)


Igris = Cichnamon("Igris", 175000006, 66754668765, 698587678)# secret
Ant_King = Cichnamon("Ant_King", 7613482, 59/10*27+3**37, 34643**52)# secret
Deer3 = Cichnamon("Deer3", 5, 22, 51)# secret
Deer4 = Cichnamon("Deer4", 3, 42, 16)# secret
Deer5 = Cichnamon("Deer5", 5, 22, 51)# secret
Deer6 = Cichnamon("Deer6", 3, 42, 16)# secret

SungJinwoo = Trainer("SungJinwoo", 0, 0)
Nokotan = Trainer("Nokotan", 0, 0)
Trebuchet = Trainer("Trebuchet", 0, 0)

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()