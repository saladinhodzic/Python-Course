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

# import random
# def pogodi_broj():
#     zamisljen_broj=random.randint(0,100)
#     ime=input("Unesite vase ime: ")
#     print("Vase ime je",ime)
#     while True:
#         nas_broj=int(input("Unesite broj "))
#         if nas_broj>zamisljen_broj:
#             print("Manje")
#         elif nas_broj<zamisljen_broj:
#             print("Vise")
#         else:
#             print("Pogodili ste broj!")
#             break
        
# pogodi_broj()

# LIST COMPREHENSION

# Zadatak je da kreirate listu koja sadrži samo samoglasnike (a, e, i, o, u) iz
# stringa "programiranje".

# string = "programiranje"
# lista = [slovo for slovo in string if slovo in 'aeiou']
# print(lista)

# Na programskom jeziku Python sastaviti f u n k c i j u koja pronalazi
# i ispisuje najdužu od učitanih reči. Reči se odvajaju razmakom. Ako
# ima više reči iste dužine ispisati prvu. Šta u kodu treba izmeniti da bi se
# ispisala poslednja takva reč.

# def najduza_rec(recenica):
#     lista=[]
#     rec=''
#     for i in range(len(recenica)):
#         if recenica[i]==" ":
#             lista.append(rec)
#             rec=''
#         rec+=recenica[i]
#     lista.append(rec)

#     najduza=''
#     for rec in lista:
#         if len(rec)>len(najduza):
#             najduza = rec
#     print("Najduza rec u recenici je",najduza)
# najduza_rec("Na primer ova recenica")

# Na programskom jeziku Python sastaviti
# program koji u zadatom tekstu prebrojava
# mala i velika slova, cifre i ostale znake.
# Obrađuje se linija po linija, sve dok se ne
# unese prazan red. U programu iskoristiti:
#  a) ugrađene funkcije: ord() i chr()
#  b) metode za rad sa stringovima: isupper(),
# islower(), isalpha() i isdigit()

tekst= input("Unesite neki tekst\n")
mala_slova=0
velika_slova=0
cifre=0
ostali=0

for slovo in tekst:
    if slovo.islower():
        mala_slova+=1
    elif slovo.isupper():
        velika_slova+=1
    elif slovo.isdigit():
        cifre+=1
    else:
        ostali+=1

print("U zadatom tekstu imamo",mala_slova,"malih slova,",velika_slova,"velikih slova",cifre,"cifara",ostali,"ostalih znakova.")