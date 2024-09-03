#Omvandla till radianer:  Obs! Frivilligt att arbeta med
#a) 160°
#b) 360°
#c) 90°
#d) Låt användaren får ange gradantalet och omvandla till radianer
#e) Låt användaren även få ange hur många decimaler programmet skall avrunda till.
#####################################################################################
import math
print(math.radians(160))
print(math.radians(360))
print(math.radians(90))
R=float(input("Vad vill du omvandla till radianer"))
print(math.radians(R))
R=float(input("Vad vill du omvandla till radianer"))
print(round(math.radians(R),int(input("Hur många decimaler vill du ha"))))