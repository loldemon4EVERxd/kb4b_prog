import random

STRANY = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
PREFERENCE = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]

def noise():
    while True:
        newprefs = []
        for xpercent in PREFERENCE:
            percent = round(random.uniform(xpercent-2, xpercent+2), 1)
            newprefs.append(percent)
        sumx = sum(newprefs)
        if sumx != 100:
            xpercent = 0
            continue
        else:
            break
    return newprefs

def ppl_partic():
    ppl = 10000000
    realpartic = random.randint(50, 80) / 100
    return ppl * realpartic

def election():
    parties = []
    snemovna = []
    total_voters = ppl_partic()
    fin_prefs = noise()
    for partyperc in fin_prefs:
        partyppl = total_voters * (partyperc / 100)
        parties.append(int(partyppl))
        if partyperc >= 5:
            snemovna.append(partyperc)
        else:
            snemovna.append('None')
    for name, hlasy, partyperc, vstupenka in zip(STRANY, parties, fin_prefs, snemovna):
        if vstupenka != 'None':
            print(f"{name} {partyperc}%  má {hlasy} hlasů", end=" ")
            while partyperc >= 1:
                print("*",end="")
                partyperc = partyperc - 1
            print()
        else:
            print(f"{name} {partyperc}%  má {hlasy} hlasů", end=" ")
            while partyperc >= 1:
                print("-",end="")
                partyperc = partyperc - 1
            print()

election()