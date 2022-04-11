import math
def prastevilo(n):
    deliteljev = 0
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            deliteljev += 1
    if deliteljev == 0:
        print(n)

for i in range (2,1001):
    prastevilo(i)