def zaporedno(a,b):
    for i in range(1,b):
        if i == 3 or 5 or 7 or 8 or 10:
            a += 31
        elif i == 2:
            a += 28
        elif i == 4 or 6 or 9 or 11:
            a += 30

       

    
    
    print("To je {} dan v letu".format(a))


d = int(input("vnesi: "))
m = int(input("vnesi: "))

zaporedno(d,m)