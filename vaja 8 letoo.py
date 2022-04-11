mesec = int(input("vnesi mesec: "))
leto = int(input("vnesi leto: "))

if mesec == 1:
    print("31 dni")
elif mesec == 2:
    if leto % 400 == 0 or leto % 100 != 0 and leto % 4 == 0:
        print("29 dni")
    else:
        print("28 dni")
elif mesec == 3:
    print("31 dni")
elif mesec == 4:
    print("30 dni")
elif mesec == 5:
    print("31 dni")
elif mesec == 6:
    print("30 dni")
elif mesec == 7:
    print("31 dni")
elif mesec == 8:
    print("31 dni")
elif mesec == 9:
    print("30 dni")
elif mesec == 10:
    print("31 dni")
elif mesec == 11:
    print("30 dni")
elif mesec == 12:
    print("31 dni")
else:
    print("napacen mesec")
