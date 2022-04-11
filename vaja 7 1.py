dT = int(input("Koliko točk si dosegel? "))
mT = int(input("Koliko je bilo možnih točk? "))
x = dT / mT
y = (dT / mT) * 100
if x > 1:
    print("vnesel si napačni vsoti poskusi še enkrat")
elif x >= 0.87:
    print("Odlična, 5", y, "%")
elif x > 0.75:
    print("Pravdobra, 4", y, "%")
elif x > 0.63:
    print("Dobra, 3", y, "%")
elif x > 0.5:
    print("Zadostna, 2", y, "%")
elif x < 0.5:
    print("Nezadostna, 1", y, "%")
