import random
import operator

operatorji = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '//': operator.floordiv}

for i in range(50):
    st1 = random.randint(1, 99)
    st2 = random.randint(1, 99)
    operacija = random.choice(list(operatorji.keys()))

    odgovor = operatorji.get(operacija)(st1, st2)

    print('koliko je {} {} {}?\n'.format(st1, operacija, st2))

    odg = int(input())

    if odg == odgovor:
        print("Bravo.")
    else:
        print("Narobe. Rezultat je ", odgovor)
