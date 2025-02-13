Str_text=str("Amazonas är världens största sammanhängande regnskog och den mest artrika skogen på hela planeten. Amazonas regnskog och floder ger oss mat, mediciner och rent vatten, och hjälper samtidigt till att reglera jordens klimat.")
lista=Str_text.split(' ')
print(len(lista))

from collections import Counter
print(lista.sort(key=len))
lista.sort(key=len)
