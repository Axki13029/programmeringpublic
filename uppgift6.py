#Räkna hypotenusan i en rätvinklig triangel där kateterna är:
#a) 3 cm och 4 cm
#b) 2 cm och 5 cm
#c) 14 cm och 11 cm
#d) Låt användaren ange kateterna själv och skriv ut hypotenusans längd.
#
#Avrunda svaren till 2 decimaler
####################################################################################################
import math
print(round(math.sqrt(3**2+4**2),2))
print(round(math.sqrt(2**2+5**2),2))
print(round(math.sqrt(14**2+11**2),2))
num1=float(input("hur lång är din katet"))
num2=float(input("Hur lång är din andra katet"))
Hypotenusa=(num1**2+num2**2)
print("din hypotenusa är",round(math.sqrt(Hypotenusa),2))
