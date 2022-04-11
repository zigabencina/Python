def vecje_manjse(a,b):
    if a > b:
        print("Prvo stevilo je vecje")
    elif a < b:
        print("Drugo stevilo je vecje")
    else:
        print("stevili sta isti")


num1 = int(input("Vnesi stevilo: "))
num2 = int(input("Vnesi stevilo: "))    

vecje_manjse(num1, num2)