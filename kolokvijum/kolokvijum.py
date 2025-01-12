# VEZBE ZA KOLOKVIJUM

# vezbe 5.

'''Napisati program u programskom jeziku Python koji
ispisuje sve parne brojeve između 1 i 20'''

# lst = [broj for broj in range(1,21) if broj % 2 == 0]
# print(lst)

'''Napisati program koji ispisuje sve proste brojeve u
opsegu od 1 do unetog broja.'''

# n = int(input("Unesite broj n: "))

# for i in range(2,n):
#     je_prost = True
#     for j in range(i-1,1,-1):
#         if i % j == 0:
#             je_prost = False
#     if je_prost:
#         print(i)

'''Na programskom jeziku Python sastaviti program
koji iz liste celih brojeva izdvaja najdužu podlistu
koja je uređena strogo rastuće. Pretpostaviti da
lista sadrži bar jedan element.'''

# lst = [1,2,3,4,5,1,2]

# trenutna_najduza = []
# najduza = []

# for i in range(len(lst)):
#     if i== 0 or lst[i] > lst[i-1]:
#         trenutna_najduza.append(lst[i])
#     else:
#         if len(trenutna_najduza) > len(najduza):
#             najduza = trenutna_najduza
#         trenutna_najduza=[lst[i]]
# if len(trenutna_najduza) > len(najduza):
#     najduza = trenutna_najduza
# print(najduza)

'''Na programskom jeziku Python sastaviti program
koji tabelira polinom.
Primer: 𝑃 𝑥 = 3𝑥
2 + 𝑥 + 4'''

# stepen = int(input("Unesite stepen polinoma: "))
# koeficijenti = [int(input("Broj: ")) for _ in range(stepen+1)]
# xmin,xmax,dx = 1.0, 10.0 , 1.5
# x = xmin
# while x <= xmax:
#     pol = 0
#     for j in range(len(koeficijenti)):
#         pol += koeficijenti[j]* x ** (stepen - j)
#     x += dx
#     print(pol)

'''8. Zadatak
20/38 Kovanice od 1,2,5,10 i 20 dinara formiraju
kvadratnu matricu para dimenzija n*n.
 Napisati program u programskom jeziku Python koji
pronalazi zbir kovanica na glavnoj dijagonali,
najmanji element iznad glavne dijagonale.'''

# import random
# coins = [1,2,5,10,20]
# n = int(input("Enter the value of n: "))

# matrix = [[random.choice(coins) for _ in range(n)]for _ in range(n)]
# diagonal = sum(matrix[i][i] for i in range(n))
# above_diagonal = list (matrix[i][j] for j in range(n) for i in range(n) if j > i)
# min_above_diagonal = min(above_diagonal)
# print(min_above_diagonal)

'''Na programskom jeziku Python sastaviti program
koji za prosleđene liste pronalazi:
 a) presek elemenata prve dve liste
 b) elemente koji se nalaze u svim listama
 c) elemente koji se nalaze u samo jednoj listi
'''

# presek = {1,2,3} & {2,3,4,5}

# liste = [[1,2,3],[3,4,5,6],[3,4,5]]
# setovi = [set(lista) for lista in liste]
# presek_svih = set.intersection(*setovi)

# razlike = set.difference(*setovi)
# print(razlike)
'''Na programskom jeziku Python sastaviti funkciju
koja proverava da li je zadata rečenica heterogram
(nijedno slovo se ne pojavljuje više od jednom).'''

# def heterogram(recenica):
#     lista = [char for char in recenica]
#     skup = set(lista)
#     if len(skup) == len(lista):
#         print("HETEROGRAM")
#     else:
#         print("NIJE HETEROGRAM")
# recenica = input("Unesite neku recenicu: ").strip()
# print(recenica)
# heterogram(recenica)

''' Na programskom jeziku Python sastaviti funkciju
koja proverava da li je zadata rečenica pangram
(sva slova se pojavljuju bar jednom)'''
# import string
# def pangram(recenica):
#     is_pangram = set(string.ascii_lowercase).issubset(recenica.lower())
#     if is_pangram:
#         print("PANGRAM")
#     else:
#         print("NIJE PANGRAM")
# recenica = input("Unesite neku recenicu: ")
# pangram(recenica)

'''Na programskom jeziku Python sastaviti funkciju
koja pronalazi srednju dužinu reči zadate datoteke.'''

# with open("tekst.txt") as file:
#     words = 0
#     letters = 0
#     for line in file:
#         words_line = file.readline().split()
#         words += len(words_line)
#         for word in words_line:
#             letters += len(word)
#     print(letters/ words)

'''Na programskom jeziku Python sastaviti program
koji:
 a) prvo čita tekst iz ulazne tekstualne datoteke i upisuje
tekst u ASCII formatu u izlaznu binarnu datoteku
 b) zatim čita podatke iz formirane binarne datoteke i
upisuje ih u izlaznu tekstualnu datoteku
'''

# a)

# import sys
# with open(sys.argv[1],encoding="utf-8") as text:
#     with open(sys.argv[2],"wb") as binary:
#         for line in text:
#             binary.write(line.encode("ascii"))

# # b)

# with open(sys.argv[2],'rb') as binary:
#     with open(sys.argv[3],'w', encoding='utf-8') as new_text:
#         for line in binary:
#             new_text.write(line.decode("ascii"))

''' Na programskom jeziku Python sastaviti funkciju
koja vrši obradu nad spiskom nadimaka:
 Ulazna datoteka u jednom redu sadrži podatke o
nadimku, polu (0 – ženski, 1 – muški) i imenima.
 Izlazna datoteka treba da grupiše imena po nadimcima.
Ako je nadimak za imena oba pola koristiti oznaku 2.'''

# import sys
# imenik = {}
# with open(sys.argv[1],encoding='utf-8') as nadimci:
#     for red in nadimci:
#         nadimak,pol,*ime = red.rstrip().split(" ")
#         ime = ', '.join(ime)
#         if nadimak not in imenik:
#             imenik[nadimak] = [pol,ime]
#         else:
#             imenik[nadimak][1] += ", " + ime
#             if imenik[nadimak][0] != pol:
#                 imenik[nadimak][0] = 2
# with open(sys.argv[2],'w',encoding='utf-8') as novi_nadimci:
#     for key , values in imenik.items():
#         novi_nadimci.write("{:6} {:<3} {}\n".format(key,values[0],values[1])) 
            
'''Na programskom jeziku Python sastaviti program
koji pronalazi ukupno vreme potrebno za obliazak
svih tvrđava na ruti unetoj sa standardnog ulaza:
 Ulazna CSV datoteka sadrži informaciju o vremenu
potrebnom da se stigne od jedne do druge tvrđave za
svaki postojeći par tvrđava
 Vreme je izraženo u minutima i isto je za oba smera
 Ruta se unosi sa standardnog ulaza, po jedan naziv
tvrđave u svakom redu i završava se praznim redom
 Ukupno vreme izraziti u satima i minutima
 Ignorisati mala i velika slova i suvišne blanko znakove'''

import sys
import csv
rute = {}
vreme= 0
with open(sys.argv[1],encoding='utf-8') as routes:
    reader = csv.reader(routes)
    for putanja in reader:
        tvrdjava1 = putanja[0].strip().lower()
        tvrdjava2 = putanja[1].strip().lower()
        vreme = int(putanja[2].strip())
        
        if tvrdjava1 not in rute:
            rute[tvrdjava1] = {}
        if tvrdjava2 not in rute:
            rute[tvrdjava2] = {}
        
        rute[tvrdjava1][tvrdjava2] = vreme
        rute[tvrdjava2][tvrdjava1] = vreme

tvrdjave = []
while True:
    tvrdjava = input("Unesite tvrdjavu: ").strip().lower()
    if tvrdjava == '':
        break
    tvrdjave.append(tvrdjava)        

for i in range(len(tvrdjave )- 1):
    tvrdjava1 = tvrdjave[i]
    tvrdjava2 = tvrdjave[i + 1]
    
    if tvrdjava1 in rute and tvrdjava2 in rute[tvrdjava1]:
        vreme+= rute[tvrdjava1][tvrdjava2]
        
sati = vreme // 60
minuti = vreme % 60
print(sati, minuti)