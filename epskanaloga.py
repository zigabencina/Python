st = int(input("Vnesi stevilo: "))
zadnja = 0
obrat = 0

while st > 0:
    zadnja = st % 10
    st = st // 10

    obrat += zadnja
    if st != 0:
        obrat = obrat * 10

print(obrat)