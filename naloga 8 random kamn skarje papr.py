import random
print(" kamen = 0, skarje = 1, papir 2")
poteza = int(input())

random = random.randint(0, 2)

if poteza == 0 and random == 2 or poteza == 1 and random == 0 or poteza == 2 and random == 1:
    print(" izgubil si")
else:
    print("zmagal si")
