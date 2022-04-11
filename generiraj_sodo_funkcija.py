import random

def generirajSodo(sp,zg):
    list = range(sp,zg)
    st = random.choice(list)
    if st % 2 == 0:
        if st <= zg and st > sp:
            st -= 2
    elif st >= sp:
        if st == 0:
            st += 1
        else:
            st -=1
    return st


print(generirajSodo(int(input("Vnesi st: ")), int(input("Vnesi st: "))))