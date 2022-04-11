stevila = []
stevec = 0

for i in range(10):
    stevilo = int(input("Vnesi stevilo: "))
    stevila.append(stevilo)

stevila.sort()

for i in range(len(stevila)):
    if stevila[i] > 5:
        stevec += 1

povprecje = sum(stevila) // 10

print("najvecje stevilo je: ", stevila[-1])
print("najmanjse je: ", stevila[0])
print("Povprečje je: ", povprecje)