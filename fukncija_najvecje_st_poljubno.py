def maks(a,b):
    if a > b:
        return True

num1 = 1
max = 0

while num1 > 0:
    num1 = int(input("vnesi: "))
    if maks(num1,max) == True:
        max = num1

print(max)

