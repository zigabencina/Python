def obrnjeno_st(a):
    obr = 0
    while a > 0:
        stevka = a % 10
        obr = obr * 10 + stevka
        a //= 10
    return obr




print(obrnjeno_st(int(input("Obrni stevilo: "))))

