def izracun(cena,pupust):
    print("cena je: ", round((cena - popust),2))
    

cena = float(input("vnesi ceno: "))
popust = (int(input("vnesi popust: ")) * 0.01) * cena
izracun(cena, popust)
