#Skriv ett program som frågar användaren efter ett tal och skriver ut om talet är jämnt eller udda.
tal=float(input("skriv ett tal"))
num=tal%2
if num == 0:
    print("ditt tal är jämnt")
elif num== 1:
    print("ditt tal är udda")
else:
    print("ditt tal är inte ett heltal")
