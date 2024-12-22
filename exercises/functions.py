# FUNCTIONS, MODULES, LIST COMPREHENSION

# Na programskom jeziku Python, napišite funkciju
# koja ispisuje poruku u formatu "Ime: [ime],
# Godine: [godine]". Vrednosti za ime i godine
# treba da se unesu preko ulaza.

# def poruka(ime,godine):
#     print("Ime:",ime,"\nGodine:",godine)
# poruka("Saladin",18)

# Na programskom jeziku Python sastaviti funkciju
# koja računa faktorijel unetog broja 𝑛. Pretpostavka
# je da se unosi nenegativan ceo broj. Zadatak rešiti:
#  a) iterativnim postupkom
#  b) rekurzijom
#  c) korišćenjem ugrađenih modula

# def faktorijel(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# recursive way
# def faktorijel(n):
#     if n == 1:
#         return n
#     return n * faktorijel(n-1)
# print(faktorijel(5))

# using modules

# import math

# def faktorijel(n):
#     print(math.factorial(n))
# faktorijel(5)

# Napisati program u programskom jeziku Python koji
# implementira dve funkcije ping i pong. Ove funkcije treba da
# budu međusobno povezane indirektnom rekurzijom, tj.
# funkcija ping poziva funkciju pong, a funkcija pong poziva
# funkciju ping.
#  Funkcija ping(i) treba da:
# Pozove funkciju pong(i-1) ako je i > 0.
# Vraća "0" ako je i == 0.
#  Funkcija pong(i) treba da:
# Pozove funkciju ping(i-1) ako je i > 0.
# Vraća "1" ako je i == 0.

# def ping(i):
#     if i>0:
#         return pong(i-1)
#     if i == 0:
#         return 0
# def pong(i):
#     if i > 0:
#         return ping(i-1)
#     if i==0:
#         return 1

# print(ping(5))

# Sastaviti funkciju za stepenovanje brojeva. Zatim napisati program u
# programskom jeziku Python koji pomaže formirane funkcije vrši računanje za
# dati broj i stepen i ispisuje rezultat.

# def stepen(broj,stepen):
#     return broj ** stepen
# print(stepen(3,3))

'''Napisati program koji implementira igricu ”Pogodi broj”.
Na početku igre računar zamišlja jedan slučajan broj u
intervalu [0,100]. Nakon toga igrač unosi svoje ime i
započinje igru. Igrač unosi jedan po jedan broj sve dok ne
pogodi koji broj je računar zamislio. Svaki put kada igrač
unese broj, u zavisnosti od toga da li je broj koji je unet
veći ili manji od zamišljenog broja ispisuje se
odgovarajuća poruka. Igra se završava u trenutku kada
igrač pogodio zamišljen broj.'''

import random
def pogodi_broj():
    zamisljen_broj=random.randint(0,100)
    ime=input("Unesite vase ime: ")
    print("Vase ime je",ime)
    while True:
        nas_broj=int(input("Unesite broj "))
        if nas_broj>zamisljen_broj:
            print("Manje")
        elif nas_broj<zamisljen_broj:
            print("Vise")
        else:
            print("Pogodili ste broj!")
            break
        
pogodi_broj()