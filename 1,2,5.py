#Skriv ett program som frågar användaren efter ett tal och skriver ut om talet är positivt, negativt eller noll.
tal=float(input("skriv dit tal"))
if tal>0:
    print("ditt tal är positivt")
elif tal <0:
    print("ditt tal är negativt")
else:
    print("ditt tal är 0")
