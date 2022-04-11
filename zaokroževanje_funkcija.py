def zaokrozevanje(a):
    a //= 10
    a *= 10
    print(a)

st = int(input("Vnesi st: "))
zaokrozevanje(st)