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
van=False
for szam in adatok:
    if 4 in adatok:
        van=True
        break

if van:
    print("Van 4-es.")
else:
    print("Nincs 4-es.")
#4. Keressük meg, hogy volt-e 5-ös
van5=False

for i in range(len(adatok)):
    if adatok[i]==5:
        van5=True
        break
if van5:
    print(f"Van 5-ös a(z) {i}. indexen.")
else:
    print("Nincs")


#5. Hány darab 9-es volt

kilenc_db=0
for szam in adatok:
    if szam==9:
        kilenc_db+=1

print(f"{kilenc_db}db 9-es van a beolvasott számok között.")
#6. Mennyi a legnagyobb beírt szám?
legnagyobbszam=adatok[0]
for szam in adatok:
    if szam>legnagyobbszam:
        legnagyobbszam=szam
print(legnagyobbszam)
    
#7. Hanyadik indexen van a legkisebb elem?
minindex=0
for i in range(len(adatok)):
    if adatok[i]<adatok[minindex]:
        minindex=i

print(f"{adatok[minindex]}, {minindex}")

#8. Páros számok kiírása.
parosszamok=[]
for szam in adatok:
    if szam%2==0:
        parosszamok.append(szam)
print(f"{parosszamok}")