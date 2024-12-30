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

# def decimal():
#     niz = input("Unesite heksadecimalni broj(najvise do 6 cifara): ").strip()
#     hex = "0123456789ABCDEF"
#     if len(niz)>6:
#         print("Uneli ste predugacak broj!")
#         return 
#     for znak in niz.upper():
#         if znak not in hex:
#             print("Niste uneli validne vrednosti!")
#             return
#     decimal=0
#     for i,znak in enumerate(reversed(niz)):
#         vrednost = int(znak,16)
#         decimal += vrednost * (16 ** i)
#     return decimal
# print(decimal())

'''5. Napisati program na programskom jeziku Python koji proverava da li je niz znakova
(string) učitan sa glavnog ulaza palindrom koji je sastavljen od tačno određenih znakova.
Palindrom je string koji se čita isto u oba smera. Program prvo treba da učita iz posebnog
reda znakove koji smeju da se pojave u stringovima, a zatim da iz narednih redova
učitava stringove i proverava da li su učitani stringovi palindromi koji se sastoje samo od
dozvoljenih znakova. Svaki string se zadaje u posebnom redu. Stringovi se mogu sastojati
od proizvoljnih znakova, a ne samo od slova. Mala i velika slova se razlikuju. Ukoliko
reč zadovoljava navedene uslove, ispisati poruku „PALINDROM“, a u suprotnom „NIJE
PALINDROM“. Program treba da ponavlja opisani postupak sve dok se sa glavnog ulaza
ne unese prazan string.
'''

# dozvoljeni_znakovi = input("Unesite dozvoljene znakove za koriscenje: ")

# def check(dozvoljeni_znakovi):
#     recenica=input("Unesite recenicu od dozvoljenih znakova: ")
#     while recenica != '':
#         for slovo in recenica:
#             if slovo not in dozvoljeni_znakovi:
#                 print("Uneli ste nevalidne vrednosti!")
#                 recenica=input("Unesite recenicu od dozvoljenih znakova: ")
        
#         palindrom=''
        
#         for slovo in range(len(recenica)-1,-1,-1):
#             palindrom += recenica[slovo]
        
#         if recenica == palindrom:
#             print("PALINDROM")
#             recenica=input("Unesite recenicu od dozvoljenih znakova: ")
            
#         else:
#             print("NIJE PALINDROM")
#             recenica=input("Unesite recenicu od dozvoljenih znakova: ")
#     return
# print(check(dozvoljeni_znakovi=dozvoljeni_znakovi))

'''8. Napisati program u programskom jeziku Python koji pronalazi torku sa najvećim
zbirom elemenata među n torki koje korisnik unosi, ispisuje sve torke čiji su svi
elementi parni, sortira torke prema drugom elementu u opadajućem redosledu'''

# n = int(input("Unesite n broj torki: "))
# niz_torki=[]

# for i in range(n):
#     torka = tuple(input("Unesite elemente torke: ").split(' '))
#     niz_torki.append(torka)

# def najveci_zbir(niz_torki):
#     suma = 0
#     max=0
#     for torka in niz_torki:
#         for broj in torka:
#             suma+=int(broj)
#         if suma > max:
#             max = suma
#         suma = 0
#     return max
# najveci_zbir(niz_torki)

# def svi_parni(niz_torki):
#     for torka in niz_torki:
#         is_true=True
#         for broj in torka:
#             if int(broj) % 2 != 0:
#                 is_true=False
#                 break
#         if is_true:
#             print(torka)
# svi_parni(niz_torki)

'''14. Napisati program u programskom jeziku Python koji računa prosek svake torke unete
od strane korisnika. Korisnik unosi broj n, zatim n torki koje sadrže po tri realna broja.
Program sortira torke prema njihovom proseku u rastućem redosledu i na kraju ispisuje
sve torke zajedno sa njihovim prosekom.
'''

# n = int(input("Unesite n broj torki: "))
# niz_torki = []

# for i in range(n):
#     torka = tuple(input("Unesite tri realna broja: ").split(" "))
#     niz_torki.append(torka)

# def prosek(torka):
#     suma=0
#     for broj in torka:
#         suma+=float(broj)
#     return suma / 3
# niz_torki.sort(key = prosek )
# print(niz_torki)

'''15. Napisati program u programskom jeziku Python koji pronalazi torku sa najmanjom
razlikom između najvećeg i najmanjeg elementa. Korisnik unosi broj n, a zatim unosi n
torki sa po tri prirodna broja'''

n = int(input("Unesite n broj torki: "))
niz_torki=[]

for i in range(n):
    torka = tuple(input("Unesite tri elementa torke: ").split(" "))
    niz_torki.append(torka)
    
def sort (torka):
    return int(max(torka)) - int(min(torka))
        

def najmanja_razlika(niz_torki):
    '''funkcija vraca torku sa najmanjom razlikom izmedju najveceg i najmanjeg elementa torke'''

    niz_torki.sort(key = sort)
    
    return niz_torki[0]
print(najmanja_razlika(niz_torki))
        