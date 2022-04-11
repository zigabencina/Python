emso = 0
stevec = 7
rezultat = 0
for e in range(12):
    emso = int(input("Vnesi emso:"))
    emso *= stevec
    stevec -= 1   
    if stevec == 1:
        stevec = 7
    rezultat += emso
print(emso,11 - rezultat % 11) 
