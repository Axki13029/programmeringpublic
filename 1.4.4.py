#Skriv ett program som testar ifall det finns dubbletter i en lista.
#Skapa sedan egna listor och testa programmet.
#Programmet skall enbart meddela användaren ifall programmet innehåller dubletter eller ej.

lista=["Karl", "Karl", "Gustav", "Maria", "Bob"]
x=0
for i in range(0,4):
    if lista.count(lista[i])>1:
        x=+1
if x>=1:
    print("Listan har dubletter")
else:
    print("Listan har inga dubletter")
        