stevilo = int(input("vnesi stevilo: "))

vsota = 0

while stevilo > 0:
    zadnja_stevka = stevilo % 10
    vsota += zadnja_stevka

    stevilo //= 10
print("vsota stevk je: ", vsota)
