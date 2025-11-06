def hod_dvema_kostkami():
    a=0
    b=0
    pokusy = 0
    while True:
        pokusy += 1
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(a, b)
        if a == b and a == 2:
            break
    print(f"pocet hodu bylo {pokusy}")