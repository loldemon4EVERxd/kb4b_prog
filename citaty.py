import random
import re

def citaty():
    cesta = "data/citaty.txt"
    
    with open(cesta, "r", encoding="utf-8") as file:
        slova = []
        for line in file:
            slovo = re.split(r"[-—]", line)
            slova.append(slovo)
    
    realemoji = []
    semoji = ["🌺", "🌼", "🌞", "🐻", "🔥"]
    femoji = ["💥", "🔥", "❤️‍", "😎", "🤣"]
    retries = random.randint(3, 5)
    for emoji in range(retries):
        realemoji.append(random.choice(semoji))
    print("Citat dne:")
    for i in range(len(realemoji)):
        print(realemoji[i], end=" ")
    print()
    dane_slovo = random.choice(slova)
    print(dane_slovo[0])
    print(f"### {dane_slovo[1].strip()} ###")
    print(random.choice(femoji))

citaty()