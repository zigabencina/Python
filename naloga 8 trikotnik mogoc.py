a = int(input())
b = int(input())
c = int(input())

if (a + b) > c and (a + c) > b and (c + b) > a:
    print("trikotnik je mogoč")
else:
    print("trikotnik ni mogoč")
