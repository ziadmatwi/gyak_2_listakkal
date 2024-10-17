import feladatok
lista=[12, 21, 56, 32, -5, -23, 35]

'''print("1.feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma: {db}")

print("2.feladat")
db:int=feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok száma: {db}")

print("3.feladat")
db:int=feladatok.ottel_oszthato(lista)
print(f"Az öttel osztható számok átlaga: {db}")

print("4.feladat")
print(f"10 érmedobás között ennyi fej található: {feladatok.fejszamlalo(feladatok.ermedobas())}")

print("5.feladat")
dobaseredmenyek=feladatok.kockaszamlalas(feladatok.kockadobas())
print("A kockadobás eredményei:")
print(f"Egyesek: {dobaseredmenyek[0]}")
print(f"Kettesek: {dobaseredmenyek[1]}")
print(f"Hármasok: {dobaseredmenyek[2]}")
print(f"Négyesek: {dobaseredmenyek[3]}")
print(f"Ötösök: {dobaseredmenyek[4]}")
print(f"Hatosok: {dobaseredmenyek[5]}")

print("6.feladat")
dobaseredmenyek=feladatok.kockaszamlalascinkelt(feladatok.kockacinkelt())
print("A kockadobás eredményei:")
print(f"Egyesek: {dobaseredmenyek[0]}")
print(f"Kettesek: {dobaseredmenyek[1]}")
print(f"Hármasok: {dobaseredmenyek[2]}")
print(f"Négyesek: {dobaseredmenyek[3]}")
print(f"Ötösök: {dobaseredmenyek[4]}")
print(f"Hatosok: {dobaseredmenyek[5]}")'''

print("5.feladat újra:")
dobások=feladatok.kockadobas()
print("A kockadobás eredményei:")
print(f"Egyesek: {feladatok.kockaszamlalasuj(dobások,1)}")
print(f"Kettesek: {feladatok.kockaszamlalasuj(dobások,2)}")
print(f"Hármasok: {feladatok.kockaszamlalasuj(dobások,3)}")
print(f"Négyesek: {feladatok.kockaszamlalasuj(dobások,4)}")
print(f"Ötösök: {feladatok.kockaszamlalasuj(dobások,5)}")
print(f"Hatosok: {feladatok.kockaszamlalasuj(dobások,6)}")


print("6.feladat újra:")
dobások=feladatok.kockacinkeltuj()
print("A kockadobás eredményei:")
print(f"Egyesek: {feladatok.kockaszamlalasuj(dobások,1)}")
print(f"Kettesek: {feladatok.kockaszamlalasuj(dobások,2)}")
print(f"Hármasok: {feladatok.kockaszamlalasuj(dobások,3)}")
print(f"Négyesek: {feladatok.kockaszamlalasuj(dobások,4)}")
print(f"Ötösök: {feladatok.kockaszamlalasuj(dobások,5)}")
print(f"Hatosok: {feladatok.kockaszamlalasuj(dobások,6)}")
