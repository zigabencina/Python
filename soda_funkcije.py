def sodo(a):
    if a % 2 == 0:
        return a + 2
    else:
        return a + 1
st = sodo(int(input("Vnesi stevilo: ")))
print(st)