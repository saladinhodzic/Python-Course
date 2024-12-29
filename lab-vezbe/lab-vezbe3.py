'''1. Na programskom jeziku Python sastaviti program koji od dva niza celih brojeva iste
dužine formira treći niz tako da bude zadovoljen uslov: c[i] = max(a[i], b[i]). Program
treba da sa glavnog ulaza učita dužinu nizova N, gde je N<200, da omogući unos
elemenata dva niza, da formira i ispiše rezultujući niz C, da koristi funkcije za unos niza,
obradu (formiranje rezultujućeg niza) i ispis rezu'''

# def unos(n):
#     niz=[]
#     for i in range(n):
#         broj = int(input(f"Unesite {i+1}. broj niza: "))
#         niz.append(broj)
#     return niz

# def formiraj(prvi,drugi,n):
#     novi=[]
#     for i in range(n):
#         novi.append(max(prvi[i],drugi[i]))
#     return novi

# def main():
#     n = int(input("Unesite duzinu nizeva: "))
#     if n >= 200:
#         return
#     prvi_niz=unos(n)
#     drugi_niz=unos(n)
    
#     novi=formiraj(prvi_niz,drugi_niz,n)
    
#     return novi

# rezultat = main()
# print(rezultat)

'''2. Napisati program na programskom jeziku Python koji sa glavnog ulaza učitava pozitivnu
dužinu niza n i elemente niza a. Smatrati da niz može imati najmanje 3, a najviše 100
elemenata i da su elementi niza realni brojevi. Program zatim treba da pronađe i na
standardnom izlazu ispiše indekse svih onih elemenata niza za koje važi da predstavljaju
aritmetičku sredinu prethodnog i sledećeg elementa. Drugim rečima, za svako i=2,...,n−1
za koje važi da je a[i]=(a[i−1]+a[i+1])/2, program treba da ispiše vrednost i. '''

# n = int(input("Unesite pozitivnu duzinu n: "))
# niz=[]
# for i in range(n):
#     broj = float(input("Unesite element niza: "))
#     niz.append(broj)

# for i in range(1,n-1):
#     if niz[i] == (niz[i-1] + niz[i+1])/2:
#         print(i)

'''4. Napisati program na programskom jeziku Python koji računa i ispisuje decimalnu
vrednost neoznačenog heksadecimalnog broja koji se učitava sa glavnog ulaza kao niz
znakova od najviše 6 karaktera. Pre računanja vrednosti, program treba da izvrši proveru
da li se u nizu nalaze samo dozvoljeni znakovi (cifre 0..9 i znakovi A..F). Ukoliko se u
nizu nalaze nedozvoljeni znakovi, ispisati odgovarajuću poruku i prekinuti izvršavanje. U
suprotnom, ispisati izračunatu decimalnu vrednost.'''

def decimal():
    niz = input("Unesite heksadecimalni broj(najvise do 6 cifara): ").strip()
    hex = "0123456789ABCDEF"
    if len(niz)>6:
        print("Uneli ste predugacak broj!")
        return 
    for znak in niz.upper():
        if znak not in hex:
            print("Niste uneli validne vrednosti!")
            return
    decimal=0
    for i,znak in enumerate(reversed(niz)):
        vrednost = int(znak,16)
        decimal += vrednost * (16 ** i)
    return decimal
print(decimal())