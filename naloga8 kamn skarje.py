import random
while True:
    print("izberi kamen, skarje ali papir")
    choice = ["kamen", "skarje", "papir"]
    poteza = input()
    random = random.choice(choice)
    print(random)
    if poteza == random:
        print("izenačeno!")
    elif poteza == "kamen":
        if random == "skarje":
            print("zmagaS!!")
        else:
            print("zgubissss")
    elif poteza == "papir":
        if random == "kamen":
            print("zmagas!")
        else:
            print("zgubiss!!")
    elif poteza == "skarje":
        if random == "skarje":
            print("zmagas!!")
        else:
            print("zgubis!")

    igrasSeenkrat = input("Gres seenkrat? (ja/ne): ")
    if igrasSeenkrat != "ja":
        break
