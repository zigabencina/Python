import random

array = ["Heads", "Tails"]
print("Ali želiš pričeti igro?")
odlo = input("")
while odlo == "Da":

    stevec = 0

    for i in range(1):
        comp = random.choice(array)
        choice = input("Ugani Heads or Tails?", "(", comp, ")")
        if choice == comp:
            stevec += 1
    print(stevec)

    print("Ali želis nadaljevati igro?")
    odlo = input("")
    if odlo == "Ne":
        break
print("nigger")
