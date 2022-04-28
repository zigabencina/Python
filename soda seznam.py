liha = [64, 39, 54, 9, 21, 90, 30, 98, 40, 34]
b = liha.copy()
soda = []

for x in b:
    if x % 2 == 0:
        soda.append(x)
        liha.remove(x)

    print(liha, soda)

print(len(liha),'soda in ', len(soda), " liha")
