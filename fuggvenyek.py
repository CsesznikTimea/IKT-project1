
#Első feladat (legkisebb szám)
def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("kérek egy számot")))  

    #print(min(tomb))

    tomb.sort()

    print(tomb[0])

feladat1()


#Második (legnagyobb szám)

def feladat2():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("kérek egy számot")))
    
    #print(max(tomb))

feladat2()


# Harmadik

def feladat3():

    pontszam=int(input("kérem a dolgozatod pontszánát: "))

    if pontszam<50:
        print("Elégtelen")

    elif pontszam<60:
        print("Elégséges")

    elif pontszam<70:
        print("Közepes")

    elif pontszam<85:
        print("Jó")

    else:
        print("Jeles")
        

