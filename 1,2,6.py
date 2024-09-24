import random
from random import randint
rand=randint(1,100)
I=input("gissa ett tal mellan 1 och 100")
if I==rand:
   print("du gissade rätt")
elif I>rand:
   print("du gissade för högt")
elif I<rand:
   print("Du gissade lågt")
