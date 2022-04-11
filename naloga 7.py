import random

st1 = random.randint(0, 100)
st2 = random.randint(0, 100)

print(st1, st2)

if st1 > st2:
    print(st1)
elif st1 < st2:
    print(st2)
else:
    print("stevili sta enaki")
