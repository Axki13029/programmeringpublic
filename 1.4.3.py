#Låt användaren skriva in fem meningar.
#Programmet skall sedan räkna ut medellängden på meningarna. 
# Programmet skall sedan skriva ut i konsolen hur lång den längsta meningen är
from collections import Counter
lista=[]
for i in range(0, 5):
    mening = input("Skriv en mening: ")
    count = mening.split(" ")  
    lista.append(count)

print("osorterad", lista)
lista.sort(key=len)
print("sorterad", lista)
print("din längsta mening är", len(lista[4]), "ord lång")
o=len(lista[0])
p=len(lista[1])
q=len(lista[2])
t=len(lista[3])
v=len(lista[4])
medelvärde=(o+p+q+t+v)/5
print("medelvärdet av dina meningar är", medelvärde)
 #använde stack overflow för att lära mig "key" och Counter
