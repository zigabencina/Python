def varcevanje(o,p,m):

    for i in range(m):
        o += p + (i+1)
    
    return o

vsota = int(input("vnesi: "))
mes_pri = int(input("vnesi: "))
st_mes = int(input("vnesi: "))

print(varcevanje(vsota,mes_pri,st_mes))

