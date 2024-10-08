#Låt användaren mata in fem tal, och spara dessa i en lista.
#Räkna på medelvärdet och medianen på dessa fem tal.
############################################################
lista=[]
x=0
for i in range(1,6):
    nummer=int(input("skriv ett tal"))
    lista.append(nummer)
    x+=nummer
b=(lista[0]+lista[1]+lista[2]+lista[3]+lista[4])/5
print("medelvärdet på talen var", b)
lista.sort()
print("medianen är", lista[2])