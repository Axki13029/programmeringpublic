#Omvandla till grader: 
#a) π radianer
#b) 2π radianer
#c) π/2 radianer
#d) Låt användaren får ange radianantalet och omvandla till grader
#e) Låt användaren även få ange hur många decimaler programmet skall avrunda till.
######################################################################################
import math
π=math.pi
print(math.degrees(π))
print(math.degrees(2*π))
print(math.degrees(π/2))
pi=float(input("vilken radian vill du omvandla till grader"))
Dec=int(input("hur mång decimaler vill du ha"))
print(round(math.degrees(pi),Dec))