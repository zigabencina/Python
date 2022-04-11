print("telesna teža?")
kg = int(input())
print("visina?")
m = int(input())
itm = kg / m ** 2
if itm < 17:
    print("Prekomerna telesna teža")
else:
    if itm > 25:
        print("prekomerna telesna teža")
    else:
        if (17 < itm) < 25:
            print("normalna telesna teža")
