import random
import re

def vyber_studenty():
    cesta = "2. prace_se_soubory/data/studenti.txt"

    with open(cesta, "r", encoding="utf-8") as file:
        gamba = random.randint(1, 5)
        studenti = []
        for student in file:
            studenti.append(student.strip())
        for student in range(gamba):
            chosen = random.choice(studenti)
            print(chosen)
            studenti.remove(chosen)

def analyza1984():
    cesta = "2. prace_se_soubory/data/1984.txt"

    with open(cesta, "r", encoding="utf-8") as file:
        text = file.read()
        yapping = text.split("PART ONE", 1)
        rest = yapping[1]
        appendix = rest.split("THE END", 1)
        winston = appendix[0]
        print(len(winston))

        
        

analyza1984()
# vyber_studenty()