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

# import sys
# import csv
# rute = {}
# vreme= 0
# with open(sys.argv[1],encoding='utf-8') as routes:
#     reader = csv.reader(routes)
#     for putanja in reader:
#         tvrdjava1 = putanja[0].strip().lower()
#         tvrdjava2 = putanja[1].strip().lower()
#         vreme = int(putanja[2].strip())
        
#         if tvrdjava1 not in rute:
#             rute[tvrdjava1] = {}
#         if tvrdjava2 not in rute:
#             rute[tvrdjava2] = {}
        
#         rute[tvrdjava1][tvrdjava2] = vreme
#         rute[tvrdjava2][tvrdjava1] = vreme

# tvrdjave = []
# while True:
#     tvrdjava = input("Unesite tvrdjavu: ").strip().lower()
#     if tvrdjava == '':
#         break
#     tvrdjave.append(tvrdjava)        

# for i in range(len(tvrdjave )- 1):
#     tvrdjava1 = tvrdjave[i]
#     tvrdjava2 = tvrdjave[i + 1]
    
#     if tvrdjava1 in rute and tvrdjava2 in rute[tvrdjava1]:
#         vreme+= rute[tvrdjava1][tvrdjava2]
        
# sati = vreme // 60
# minuti = vreme % 60
# print(sati, minuti)

'''Napisati program u programskom jeziku Python koji učitava
datoteku sa ocenama učenika. Svaka linija u datoteci sadrži
ime učenika i njegovu ocenu. Program treba da učita
podatke i kreira rečnik gde je ime učenika ključ, a lista
ocena vrednost. Nakon toga, ispisati prosečnu ocenu za
svakog učenika.'''

# import sys
# dnevnik = {}
# with open(sys.argv[1],encoding='utf-8') as ocene:
#     for red in ocene:
#         ime,ocena = red.strip().split(" ")
#         if ime not in dnevnik:
#             dnevnik[ime] = [int(ocena)]
#         else:
#             dnevnik[ime] += [int(ocena)]
# srednje_ocene = {ime:sum(ocena for ocena in dnevnik[ime]) / len(dnevnik[ime]) for ime in dnevnik}
# print(srednje_ocene)
            
'''U svakom redu tekst datoteke katalog.txt se nalaze podaci o
filmovima raspoloživim u nekom DVD klubu. Prvi podatak je
celobrojna šifra, zatim celobrojna oznaka regiona, na kraju
sledi ime filma koje nije duže od 70 znakova. Napraviti
program koji u novu tekst datoteku sifre.txt zapisuje sve
šifre koje se u ulaznoj tekst datoteci pojavljuje više puta
(bar dva puta). Svaku takvu šifru u izlaznu datoteku upisati
samo jednom. Broj zapisa u ulaznoj datoteci, kao ni najveća
vrednost šifre nisu unapred poznati. Ulaznu datoteku je
dozvoljeno čitati samo jednom. Voditi računa o ispravnoj
alokaciji i dealokaciji svih potrebnih resursa.'''

# import sys
# novi_katalog = {}
# with open(sys.argv[1]) as katalog:
#     for film in katalog:
#         sifra, oznaka, *ime = film.rstrip().split(" ")
#         ime = " ".join(ime)
#         if sifra in novi_katalog:
#             novi_katalog[sifra] += [sifra]
#         if sifra not in novi_katalog:
#             novi_katalog[sifra] = [sifra]
# with open(sys.argv[2],'a') as sifre:
#     for sifra in novi_katalog:
#         if len(novi_katalog[sifra]) > 1:
#             sifre.write(f"{sifra}\n")

'''Na programskom jeziku Python sastaviti program
koji ispisuje pozicije pojavljivanja reči u tekstu.'''

# import re
# rec = re.compile(input("Unesite rec za pretragu: "))
# tekst = input("Unesite neki tekst: ")

# for pogodak in rec.finditer(tekst):
#     print(pogodak.start())

'''Na programskom jeziku Python sastaviti funkciju
koja pronalazi godine izbora u zvanje saradnika u
nastavi i ispisuje ih na standardnom izlazu sortirane
u opadajućem poretku.'''
# import re
# fajl = input("Unesite ime fajla za pretragu: ")

# def find_sort(fajl):
#     with open(fajl) as fajl:
#         text = fajl.read()
#     sablon = re.compile(r"\d\d\d\d")
#     godine = sablon.findall(text)
#     sort_godine = sorted(godine,reverse=True)
#     return sort_godine
# print(find_sort(fajl))

'''Na programskom jeziku Python sastaviti funkciju
koja prosleđenoj datoteci menja format u kom su
zapisani podaci o studentu.
'''
# import re
# def formatiraj(students):
#     with open(students,'r+',encoding='utf-8') as studenti:
#         sadrzaj = studenti.read()
#         sablon = re.compile(r"\d{1,4}/\d{2}(\d{2}),\s+(\w+)\s+(\w+)")
#         novi_sablon = sablon.sub(r"\2/\1, \4 \3",sadrzaj)
#         studenti.seek(0)
#         studenti.truncate()
#         studenti.write(novi_sablon)
# formatiraj("./studenti/studenti.csv")

'''Primicemo fajl razgovori.txt koji sadrzi imena osoba,datume i intervale razgovora izmedju osoba, nas zadatak je da ispisemo datume za svaku osobu kada je vodila najduzi razgovor'''

# import sys
# import re
# # funkcija za formatiranje intervala

# def formatiraj(interval):
#     pocetak,kraj = interval.split('-')
#     h1,min1 = map(int,pocetak.split(':'))
#     h2,min2 = map(int,kraj.split(':'))
#     return (h2 * 60 + min2) - (h1*60+min1)
# sablon = re.compile( r"(\w+)\s+(\w+)\s+(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}-\d{2}:\d{2})")
# imenik = {}
# with open(sys.argv[1],'r',encoding='utf-8') as razgovori:
#     for linija in razgovori:
#         is_match = sablon.match(linija.strip())
#         if is_match:
            
#             prvo_ime,drugo_ime,datum,interval = is_match.groups()
#             trajanje = formatiraj(interval)
            
#             for ime in [prvo_ime,drugo_ime]:
#                 if ime not in imenik or trajanje > imenik[ime]['trajanje']:
#                     imenik[ime] = {"datum":datum,"trajanje":trajanje}
# for k,v in imenik.items():
#     print(k,v)

'''Na programskom jeziku Python sastaviti program
koji pronalazi i ispisuje sve nekorektne e-mail
adrese iz zadatate datoteke. Smatrati da korektna
adresa ima oblik local@domain pri čemu važi
sledeće:
 Oba dela adrese (local i domain) smeju da sadrže slova,
brojeve, tačke, crtice i pluseve
 Oba dela adrese moraju da počinju slovom
 Prvi deo (local) ne sme da ima više od 64 karaktera
 Drugi deo (domain) mora da se završi tačkom praćenom
sa dva ili tri slova'''

# import re

# sablon = re.compile(r"^[a-zA-Z][\w.+-]{0,63}@[a-zA-Z][\w.+-]*\.[a-zA-Z]{2,3}$")

# with open("./domeni/domeni.txt") as file:
#     for line in file:
#         match = sablon.search(line)
#         if not match:
#             print(line)
