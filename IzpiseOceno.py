import random

def izpisiOceno(a):
    if a == 0:
        print("NPS")
    elif a == 1:
        print("Nezadostno")
    elif a == 2:
        print("Zadostno")
    elif a == 3:
        print("Dobro")
    elif a == 4:
        print("Pravdobro")
    elif a == 5:
        print("Odlično")
    else:
        print("napacna ocena")
        
for i in range(30):
    izpisiOceno(random.randint(0,5))