import random

pin = random.randint(1000, 9999)
print(pin)
st = int(input("Vnesi pin: "))

while st != pin:
    print("Vnesli ste napačen pin")
    st = int(input("Vnesi pin: "))
else:
    print("Pravilen pin!")
