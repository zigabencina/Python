#Napisi funkcijo ki prejme poljubno celo stevilo, nato pa to stevilo obrne in vrne
from calendar import prcal


def obrnjeno(a):
    obr = 0
    stevec = 1000
    prva_nic = False
    while a > 0:
        if stevec == 1000 and a % 10 == 0:  
            prva_nic = True
        stevka = a % 10
        obr = obr * 10 + stevka
        a = a // 10
        stevec -= 1
    if prva_nic:
        return "0" + str(obr)
    else: 
        return obr




print(obrnjeno(int(input("Vnesi število: "))))