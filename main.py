def LenkuParbaude(Len1,Len2,Len3):
  rezultats = False
  if Len1+Len2+Len3==180:
    rezultats = True
  return rezultats

Len1 = int(input("Ievadiet 1.leņķi: "))
Len2 = int(input("Ievadiet 1.leņķi: "))
Len3 = int(input("Ievadiet 1.leņķi: "))
rez = LenkuParbaude(Len1,Len2,Len3)
if rez:
  print("Trīsstūris eksistē!")
else:
  print("Trīsstūris neeksistē!")



skait=0
while skait<=100:
  if skait%2!=0:
    print(skait)
  skait+=1


from math import *
skait=-5
while skait<=25:
  print(cos(skait)**2)
  skait+=2


teksts=input("ievadi tekstu")
skaititajs=0
for burts in teksts:
  if burts=="c":
    skaititajs+=1
print(("Burtu a skaits ="),skaittitajs)
  