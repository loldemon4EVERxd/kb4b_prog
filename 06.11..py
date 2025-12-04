import random
from operator import add, sub, mul
import re

SPRAVNE = 0
OPS = (add, sub, mul)

def generuj_priklad():
    a, b = random.randint(0,10), random.randint(0,10)
    op = random.choice(OPS)
    if op == add:
        znak = "+"
        zadani = a + b
    elif op == sub:
        znak = "-"
        zadani = a - b
    else:
        znak = "*"
        zadani = a * b
    odpoved = input(f"{a} {znak} {b} = ")
    if int(odpoved) == int(zadani):
        global SPRAVNE
        SPRAVNE += 1

def nacti_priklady():
    cesta = "2. prace_se_soubory/data/priklady.txt"

    with open(cesta, "r", encoding="utf-8") as file:
        priklady = []
        for priklad in file:
            priklad = re.split(r" ", priklad)
            priklady.append(priklad)
            if priklad[1] == "+":
                zadani = priklad[0] + priklad[2]
            elif priklad[1] == "-":
                zadani = priklad[0] - priklad[2]
            else:
                zadani = priklad[0] * priklad[2]
            odpoved = input(f"{priklad[0]} {priklad[1]} {priklad[2]} = ")
            if int(odpoved) == int(zadani):
                global SPRAVNE
                SPRAVNE += 1
    print(f"Spravne jsi mel {SPRAVNE}/{len(priklady)} prikladu")
    SPRAVNE = 0

def quiz():
    cesta = "2. prace_se_soubory/data/otazky.csv"
    
    with open(cesta, "r", encoding="utf-8") as file:
        priklady = []
        skip = 0
        for line in file:
            if skip == 0:
                skip += 1
                continue
            priklad = re.split(r";", line)
            priklady.append(priklad)
            print(priklad[0])
            print(f"A) {priklad[1].strip()}")
            print(f"B) {priklad[2].strip()}")
            print(f"C) {priklad[3].strip()}")
            odpoved = input("Tva odpoved: ")
            if odpoved == priklad[4].strip():
                global SPRAVNE
                SPRAVNE += 1
            print()
    print(f"Spravne jsi mel {SPRAVNE}/{len(priklady)} prikladu")
    SPRAVNE = 0


# for i in range(3):
#     generuj_priklad()
# print(f"Spravne jsi mel {SPRAVNE}/3 prikladu")

# nacti_priklady()

quiz()