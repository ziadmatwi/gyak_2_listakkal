import feladatok
lista=[12, 21, 56, 32, -5, -23, 35]

print("1.feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma: {db}")

print("2.feladat")
db:int=feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok száma: {db}")

print("3.feladat")
db:int=feladatok.ottel_oszthato(lista)
print(f"Az öttel osztható számok átlaga: {db}")

print(feladatok.ermedobas())