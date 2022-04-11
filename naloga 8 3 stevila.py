import random

st1 = random.randint(0, 100)
st2 = random.randint(0, 100)
st3 = random.randint(0, 100)


# -- najprej izpise najmanjse --

if st1 <= st2 and st1 <= st3:
    print(st1)

elif st2 <= st1 and st2 <= st3:
    print(st2)

else:
    print(st3)

# -- srednje stevilo --
if st1 > st2 and st1 < st3 or st1 < st2 and st1 > st3:
    print(st1)

elif st2 > st1 and st2 < st3 or st2 < st1 and st2 > st3:
    print(st2)

else:
    print(st3)

# -- najvecje stevilo --
if st1 >= st2 and st1 >= st3:
    print(st1)

elif st2 >= st1 and st2 >= st3:
    print(st2)

else:
    print(st3)
