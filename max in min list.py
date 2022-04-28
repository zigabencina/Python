s = []

for i in range(10):
    a = int(input('Vnesi stevilo: '))
    if a % 2 == 0:
        s.append(a)

print(max(s), min(s))