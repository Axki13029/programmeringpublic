Lista=[]
x=input("hur många hundar har du")
print(x)
if x==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49 or 50 or 51 or 52 or 53 or 54 or 55 or 56 or 57 or 58 or 59 or 60 or 61 or 62 or 63 or 64 or 65 or 66 or 67 or 68 or 69 or 70 or 71 or 72 or 73 or 74 or 75 or 80 or 85 or 90 or 95 or 99 or 100 or 101 or 105 or 110 or 115 or 120 or 125 or 150 or 175 or 200 or 225 or 250 or 275 or 300 or 350 or 400 or 450 or 500 or 550 or 600 or 650 or 700 or 750 or 800 or 850 or 900 or 950 or 1000 or 1100 or 1200 or 1300 or 1400 or 1500 or 1600 or 1700 or 1800 or 1900 or 2000 or 2200 or 2400 or 2600 or 2500 or 2800 or 3000 or 3200 or 3400 or 3500 or 3600 or 3800 or 4000 or 4200 or 4400 or 4500 or 4600 or 4800 or 5000:True
if True:
    for i in range(1,int(x)+1):
            Namn=input("vad heter din hund")
            Ras=input("vilken ras är den")
            Vikt=input("hur mycket väger den")#låter användaren bestämma variablrna som ska läggas in i listan
            Lista.append({"namn": Namn, "ras": Ras, "vikt": Vikt}) #lägger till alla hundens egenskaper i listan
else:
        print("Error, använd siffror")
print(Lista)