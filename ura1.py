u = int(input("vnesi uro: "))
minuta = int(input("vnesi minuto: "))

if minuta < 30:
    print("ura je ", minuta, "minut čez ", u)
elif minuta > 30:
    print("ura je ", 60 - minuta, "minut do ", u)
elif minuta == 30:
    print("ura je pol ", u)
elif minuta == 0:
    print("ura je", u)
