def ura_min(u, m):
    if m == 30:
        print("ura je pol {} ".format(u+1))
    elif m > 30:
        print("ura je {} do {}".format(abs(m-60), u))
    elif m < 30 and m > 0:
        print("ura je {} čez {}".format(m, u))
    else:
        print("ura je {} ".format(u))



ura_min(int(input("Vnesi stevilo: ")),int(input("Vnesi stevilo: ")))