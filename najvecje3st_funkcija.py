def primerjava(a,b,c):
    if a > b:
        if a > c:
            print("najvecje je prvo")
    if b > a:
        if b > c:
            print("Najvecje je drugo")
    if c > a:
        if c > b:
            print("najvecje je tretje")
    if a == b and b == c:
        print("Stevila so enaka")



num1 = int(input("Vnesi stevilo: "))
num2 = int(input("Vnesi stevilo: "))
num3 = int(input("Vnesi stevilo: "))

primerjava(num1,num2,num3)