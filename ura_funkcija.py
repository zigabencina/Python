def ura(u,m):
    if m < 30:
        print("ura je {} do {}").format(m, u)
    elif m > 30:
        print("ura je {} čez {}").format(m, u)
    elif m == 30:
        print("ura je pol {}").format(u)
    else:
        print("ura je {}").format(u)

ura = int(input("Vnesi stevilo: "))
min = int(input("Vnesi stevilo: "))