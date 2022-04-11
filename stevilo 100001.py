import math

stevec = 0
stevilo = 1.00001
st = int(input("Vnesi število: "))

while stevilo <= st:
    st = math.sqrt(st)
    if st > stevilo:
        stevec += 1

print("STevilo smo korenili: ", stevec)
