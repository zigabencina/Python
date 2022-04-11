stevilo = input("vnesi stevilo: ")
stevec = 0
for stevka in stevilo:
    for mesto in stevka:
        if mesto == "0" or mesto == "9" or mesto == "8" or mesto == "6":
            stevec += 1
        
stevka = int(stevka)
stevka = stevka // 2
if stevec > stevka:
    print("stevilo je luknjasto")
else:
    print("stevilo ni luknjasto")
