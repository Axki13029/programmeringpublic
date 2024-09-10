#E = 25
#D = 30
#C = 35
#B = 40
#A = 45
E=int(25)
D=int(30)
C=int(35)
B=int(40)
A=int(45)
P=int(input("Hur många poäng fick du")) #P står för poäng
if P<0:
    print("Error, det är inte möjligt att få mängden poäng du skrev in testa igen")
elif P<25:
    print("F")
elif P<30:
    print("E")
elif P<35:
    print("D")
elif P<40:
    print("C")
elif P<45:
    print("B")
elif P<51:
    print("A")
else:
    print("Error, det är inte möjligt att få mängden poäng du skrev in testa igen")