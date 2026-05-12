nejdelsiprodleva = 0
salinyvjednuhodinu = 1
hodinavkterouprojelonejvicsalin = 0
nejvicsalinvjednuhodinu = 1
while True:
    print("saliny musi byt aspon 2 a jejich odjezdy musi byt serazeny vzestupne")
    pocetsalin = int(input("zadej pocet salin "))
    if pocetsalin > 1:
        break
while True:
    print("1. salina")
    hodiny1 = int(input("zadej hodiny "))
    minuty1 = int(input("zadej minuty "))
    if (-1 < hodiny1 < 24) and (-1 < minuty1 < 61):
        break
odjezdsaliny1 = hodiny1 * 60 + minuty1
for i in range(2, pocetsalin + 1):
    while True:
        print(f"{i}. salina")
        hodiny = int(input("zadej hodiny "))
        minuty = int(input("zadej minuty "))
        if (-1 < hodiny < 24) and (-1 < minuty < 60):
            break
    odjezdsaliny = hodiny * 60 + minuty
    if i == 2:
        if hodiny == hodiny1:
            salinyvjednuhodinu += 1
            hodinavkterouprojelonejvicsalin = hodiny
            nejvicsalinvjednuhodinu += 1
        minulehodiny = hodiny
        if odjezdsaliny > odjezdsaliny1:
            prodleva = odjezdsaliny - odjezdsaliny1
            prodlevahodiny = prodleva // 60
            prodlevaminuty = prodleva % 60
            print(f"prodleva mezi odjezdy je {prodlevahodiny} hodin/hodina/hodiny a {prodlevaminuty} minut/minuta/minuty")
            minulyodjezd = odjezdsaliny
            nejdelsiprodleva = prodleva
        elif odjezdsaliny1 == odjezdsaliny:
            print("saliny maji stejny odjezd")
        else:
            print("*ajejichodjezdymusibytserazenyvzestupne*")
    else:
        if hodiny == minulehodiny:
            salinyvjednuhodinu += 1
            if salinyvjednuhodinu > nejvicsalinvjednuhodinu:
                nejvicsalinvjednuhodinu += 1
                hodinavkterouprojelonejvicsalin = hodiny
        if minulehodiny != hodiny:
            salinyvjednuhodinu = 1
        minulehodiny = hodiny
        if odjezdsaliny > minulyodjezd:
            prodleva = odjezdsaliny - minulyodjezd
            prodlevahodiny = prodleva // 60
            prodlevaminuty = prodleva % 60
            print(f"prodleva mezi odjezdy je {prodlevahodiny} hodin/hodina/hodiny a {prodlevaminuty} minut/minuta/minuty")
            minulyodjezd = odjezdsaliny
            if prodleva > nejdelsiprodleva:
                nejdelsiprodleva = prodleva
        elif minulyodjezd == odjezdsaliny:
            print("saliny maji stejny odjezd")
        else:
            print("*ajejichodjezdymusibytserazenyvzestupne*")

nejdelsiprodlevahodiny = nejdelsiprodleva // 60
nejdelsiprodlevaminuty = nejdelsiprodleva % 60
print("")
print(f"nejdelsi prodleva mezi odjezdy je {nejdelsiprodlevahodiny} hodin/hodina/hodiny a {nejdelsiprodlevaminuty} minut/minuta/minuty")
print(f"nejvice jelo/jela/jely {nejvicsalinvjednuhodinu} salin/salina/saliny v/ve {hodinavkterouprojelonejvicsalin} hodin/hodinu/hodiny")