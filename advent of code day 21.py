#Player 1 starting position: 7
#Player 2 starting position: 3
array = []

player1 = 7
player1s = 1
player2 = 3
player2s = 4

stevec = 0
for i in range(100000):
    array.append(i)
    for u in range(len(array)):
        array.append(u)
    print(array)
