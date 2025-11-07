#1. Adatok beolvasása listába
adatok=[]
with open ("data.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        adatok.append(int(sor))

print(adatok)


#2. Adatok átlaga

szam_db=0
osszeg=0
for szam in adatok:
    osszeg+=szam
    szam_db+=1

atlag=osszeg/szam_db

print(f"A beolvasott adatok átlaga {atlag}")

#3. Döntsük el, hogy volt-e 4-es
#4. Keressük meg, hogy volt-e 5-ös
#5. Hány darab 9-es volt
#6. Mennyi a legnagyobb beírt szám?
#7. Hanyadik indexen van a legkisebb elem?
#8. Páros számok kiírása.