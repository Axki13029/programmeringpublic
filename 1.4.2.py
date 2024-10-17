#Låt användaren får mata in temperaturmätningar på en väderstation. 
#Dessa mätningar skall sparas i en lista och användaren skall få skriva så många som den vill.
#När programmet är färdigt skall listan med alla mätningar skrivas ut och även medeltemperaturen.
lista=[]
x=int(input("Skriv hur många temperaturer vill du mata in"))
for i in range(0,x):
    temperatur=float(input("Mata in en temperatur"))
    lista.append(temperatur)
print(lista)
G=int(len(lista))
U=sum(lista)/G
print(U)
