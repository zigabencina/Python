def popust(p,eur):
    p = (p / 100) * eur
    eur -= p
    return eur

euro = int(input("Vnesi eur: "))
popusti = int(input("Vnesi popust: "))

print(popust(popusti,euro))