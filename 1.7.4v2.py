Lista=[]

try:
    x=int(input("hur många hundar har du"))
except ValueError:
    print("använd hela siffror")
if x==int:
    for i in range(1,x+1):
        Namn=input("vad heter din hund")
        Ras=input("vilken ras är den")
        Vikt=input("hur mycket väger den")#låter användaren bestämma variablrna som ska läggas in i listan            Lista.append({"namn": Namn, "ras": Ras, "vikt": Vikt}) #lägger till alla hundens egenskaper i lista
print(Lista)
