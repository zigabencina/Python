import random

znesek = int(input("Vnesi znesek: "))
profit = ()


for i in range(30):
    profit = random.randint(-5,6) * 0.01

    znesek += znesek * profit

    print("Današnji profit je: ", profit, " in trenutni znesek je: ", znesek," Današnji dan je: ",i)

