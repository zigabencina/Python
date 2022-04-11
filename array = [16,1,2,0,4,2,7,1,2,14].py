array = [16,1,2,0,4,2,7,1,2,14]
dest  = 2
dest1 = 1
dest2 = 10
dest3 = 3
destx = ()
destFinal = 0
destFinal1 = 0
destFinal2 = 0
destFinal3 = 0
destFinalx = 0

for i in range(len(array)):
    if (array[i] > 2):
        destStore = array[i] - dest
    else:
        destStore = dest - array[i]
    destFinal = destFinal + destStore
    

print(destFinal, " Alligna se at 2")

for i in range(len(array)):
    if (array[i] > 1):
        destStore1 = array[i] - dest1
    else:
        destStore1 = dest1 - array[i]
    destFinal1 = destFinal1 + destStore1

print(destFinal1, " Alligna se at 1")

for i in range(len(array)):
    if (array[i] > 3):
        destStore3 = array[i] - dest3
    else:
        destStore3 = dest3 - array[i]
    destFinal3 = destFinal3 + destStore3

print(destFinal3, "Alligna se at 3")


for i in range(len(array)):
    if (array[i] > 10):
        destStore2 = array[i] - dest2
    else:
        destStore2 = dest2 - array[i]
    destFinal2 = destFinal2 + destStore2

print(destFinal2, "Alligna se at 10")

for destx in range(0,10):
    for i in range(len(array)):
        if (array[i] > 3):
            destStorex = array[i] - destx
        else:
            destStorex = destx - array[i]
        destFinalx = destFinalx + destStorex
    print(destFinalx, "Alligna se at ", destx)
    destFinalx = 0
print("najmanj goriva uporabi ce se na 0  alligna")





