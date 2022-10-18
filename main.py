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