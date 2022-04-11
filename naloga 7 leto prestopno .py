leto = int(input())
if leto % 4 == 0:
    if leto % 100 == 0:
        if leto % 400 == 0:
            print("leto je prestopno")
        else:
            print("Leto ni prestopno")
    else:
        print("leto je prestopno")
else:
    if leto % 100 == 0:
        if leto % 400 == 0:
            print("leto je prestopno")
        else:
            print("Leto ni prestopno")
    else:
        print("leto je prestopno")
