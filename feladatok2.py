#feladat 0
szam=-1
while True:
    szam=int(input("Kérek egy számot 1-20 között:"))
    if(szam>0 and szam <=20): break

sor=""
for i in range(szam):
    sor+=""
    
print(sor+"START")

#feladat 1
def betusit():
    szo=input("Kérek egy szót:")
for i in range (len(szo)-1,-1,-1):
    print(szo[i].upper())
    
betusit()

#feladat2
bekert_szo=input("Kérek egy szót:")
for karakter in bekert_szo:
    print(karakter)
    
#feladat5
def mezot_rajzol(sor,oszlop):
    for s in range(sor):
        for o in range(oszlop):
            print("*", end="")
        print()