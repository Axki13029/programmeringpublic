#Programmet ska kunna kasta en specifierad mängd tärningar och räkna ut medelvärdet samnt totalla summan
import random
num=int(input("hur många gånger vill du kasta"))
for i in range (1,num+1):
    kast=random.randint(1,6)
