#Låt användaren skriva in fem meningar.
#Programmet skall sedan räkna ut medellängden på meningarna. 
# Programmet skall sedan skriva ut i konsolen hur lång den längsta meningen är
from collections import Counter
lista=[]
for i in range(0, 5):
    men = input("Skriv en mening: ")
    countmen = men.split(" ")  
    lista.append(countmen)  

print("osorterad", lista)
lista.sort(key=len)
print("sorterad", lista)
print("din längsta mening är", len(lista[4]), "ord lång")
print("Medel längden på dina meningarär", (len(lista[0])+len(lista[1])+len(lista[2])+len(lista[3])+len(lista[4])/5))
 #använde stack overflow för att lära mig "key" och Counter
