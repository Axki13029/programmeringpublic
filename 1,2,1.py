biljett=int(50)
årskort=int(499)
antal=int(input("hur många gånger kommer du gå till gymet"))
if biljett*antal<=årskort:
     print("du borde köpa biljetter")
elif biljett*antal>årskort:
     print("du borde köpa årskort")