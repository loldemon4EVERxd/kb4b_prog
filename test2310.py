import random

def hod_dvema_kostkami():
    a=0
    b=0
    pokusy = 0
    while True:
        pokusy += 1
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(a, b)
        if a == b:
            break
    print(f"pocet hodu bylo {pokusy}")

def vypis_statistiky():
    temps = []
    tsoucet = 0
    podbodem = 0
    for i in range(24):
        teplota = random.randint(-10, 20)
        temps.append(teplota)
        tsoucet += teplota
        if teplota < 0:
            podbodem += 1
    prumerdne = tsoucet / 24
    print(f"namerene teploty:", end=" ")
    for temp in temps:
        print(temp, end=" ")
    print()
    print(f"prumer dne je: {prumerdne:.2f} °C")
    print(f"pod bodem mrazu je {podbodem} teplot")

def generuj_priklad():
    spravne = 0
    for i in range(3):
        zadani = random.randint(0, 5)
        xzadani = zadani * zadani
        odpoved = input(f"sqrt({xzadani}) = ")
        if int(odpoved) == int(zadani):
            spravne += 1
    print(f"Spravne jsi mel {spravne}/3 prikladu")
    if spravne == 3:
        return True # vsechny priklady jsou spravne 
    else:
        return False # nektere priklady jsou spatne

hod_dvema_kostkami()
# print()
# vypis_statistiky()
# print()
# generuj_priklad()