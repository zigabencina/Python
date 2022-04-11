def sestej():
    sestevek = 0
    kvadrat = 1
    for i in range(64):
        print(kvadrat)
        sestevek += kvadrat 
        kvadrat *=  2
    return sestevek

print(sestej())
