#Låt användaren får mata in temperaturmätningar på en väderstation. 
#Dessa mätningar skall sparas i en lista och användaren skall få skriva så många som den vill.
#När programmet är färdigt skall listan med alla mätningar skrivas ut och även medeltemperaturen.
lista=[]
x=0
for i in range(1,6):
    nummer=int(input("skriv ett tal"))
    lista.append(nummer)
    x+=nummer