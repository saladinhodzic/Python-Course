'''1. Na programskom jeziku Python sastaviti program koji od dva niza celih brojeva iste
dužine formira treći niz tako da bude zadovoljen uslov: c[i] = max(a[i], b[i]). Program
treba da sa glavnog ulaza učita dužinu nizova N, gde je N<200, da omogući unos
elemenata dva niza, da formira i ispiše rezultujući niz C, da koristi funkcije za unos niza,
obradu (formiranje rezultujućeg niza) i ispis rezu'''

def unos(n):
    niz=[]
    for i in range(n):
        broj = int(input(f"Unesite {i+1}. broj niza: "))
        niz.append(broj)
    return niz

def formiraj(prvi,drugi,n):
    novi=[]
    for i in range(n):
        novi.append(max(prvi[i],drugi[i]))
    return novi

def main():
    n = int(input("Unesite duzinu nizeva: "))
    if n >= 200:
        return
    prvi_niz=unos(n)
    drugi_niz=unos(n)
    
    novi=formiraj(prvi_niz,drugi_niz,n)
    
    return novi

rezultat = main()
print(rezultat)