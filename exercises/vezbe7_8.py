# NIZOVI MATRICE TORKE

# Na programskom jeziku Python sastaviti program
# koji pronalazi i ispisuje treći i posednji element
# niza

# niz = input("Unesite niz brojeva\n").split(" ")

# print(f"Treci element niza {niz[2]} a zadnji je {niz[-1]}")

# Na programskom jeziku Python sastaviti program
# koji računa zbir svih elemenata niza.

# niz = input("Unesite brojeve: ").split(" ")
# suma=0
# for broj in niz:
#     suma+=int(broj)
# print(suma)

# Na programskom jeziku Python sastaviti program
# koji sa standardnog ulaza unosi elemenata niza i
# sortira niz u rastućem redosledu

# niz = input("Unesite brojeve niza\n").split(" ")

# novi_niz=[int(broj) for broj in niz]

# novi_niz.sort()
# print(novi_niz)

# Na programskom jeziku Python sastaviti program koji rotira
# niz ulevo za k pozicija. Na primer, ako je niz [1, 2, 3, 4, 5] i
# k = 2, rezultat bi bio [3, 4, 5, 1, 2]

# niz = input("Unesite brojeve niza\n").split(" ")

# niz=[int(x) for x in niz]

# k= int(input("Unesite broj pozicija za rotaciju: "))

# rotiran_niz= niz[k:] + niz[:k]

# print(rotiran_niz)

'''Na programskom jeziku Pythonu sastaviti program
koji od dva niza celih brojeva iste dužine formira
treći niz tako da bude zadovoljen uslov: c[i] =
max(a[i], b[i]). Program treba da sa glavnog ulaza
da učita dužinu nizova N, gde je 𝑁<200, da
omogući unos elemenata dva niza, da formira i
ispiše rezultujući niz C, da koristi funkcije za:unos
niza,obradu (formiranje rezultujućeg niza),ispis
rezultata. Program se ponavlja sve dok korisnik ne
unese nevalidnu vrednost za 𝑁(npr. 𝑁≥200 ili 𝑁≤0).'''

# def unos(n):
#     niz=[]
#     for _ in range(n):
#         broj = int(input(f"Unesite {_+1}. broj niza "))
#         niz.append(broj)
#     return niz

# def formiraj(prvi,drugi,n):
#     novi_niz=[]
#     for i in range(n):
#         novi_niz.append(max(prvi[i],drugi[i]))
#     return novi_niz
# while True:
#     n=int(input("Unesite duzinu dva niza: "))
#     if n>=200 or n<=0:
#         break
    
#     prvi_niz=unos(n)
#     drugi_niz=unos(n)
    
#     novi = formiraj(prvi_niz,drugi_niz,n)
#     print(novi)

'''MATRICE'''

# Na programskom jeziku Python sastaviti program
# koji učitatava realnu matricu dimenzija n*m.
# Ispisati novu matricu koja se sastoji od recipročnih
# vrednosti elemenata unete matrice.

# n=int(input("Unesite n redova matrice "))
# m=int(input("Unesite m kolona matrice "))
# matrica=[]
# for i in range(n):
#     red=[]
#     for j in range(m):
#         red.append(int(input("Unesite broj matrice ")))
#     matrica.append(red)
# for i in range(n):
#     print(matrica[i])
        
'''Na programskom jeziku Python napisati pogram
koji za odeljenje od najviše 25 učenika i najviše 15
predmeta izračunava:
 prosečne ocene učenika
 prosečne ocene po predmetima na osnovu tabele
ocena iz dnevnika. '''

# ucenici=int(input("Unesite broj ucenika: "))
# predmeti = int(input("Unesite broj predmeta: "))

# ocene=[]
# # inputing grades from each student into the array
# for i in range(ucenici):
#     ocene_ucenika=[]
#     for j in range(predmeti):
#         ocena = int(input(f"Unesite ocenu {i+1}. ucenika\n"))
#         ocene_ucenika.append(ocena)
#     ocene.append(ocene_ucenika)

# arit_ocene=[]
# # finding arithmetic mean of grades from each student
# for ucenik in ocene:
#     suma=sum(ucenik)
#     arit_ocene.append(suma/len(ucenik))

# arit_predmeta=[]

# for j in range(predmeti):
#     suma=0
#     for i in range(ucenici):
#         suma+=ocene[i][j]
#     arit_predmeta.append(suma/predmeti)
# print(arit_predmeta)

'''TORKE'''

# Na programskom jeziku Python sastaviti program
# koji izračunava prosečnu vrednost svih elemenata u
# torki brojeva..

# torka=(1,2,3,4,5)
# suma=0
# for i in torka:
#     suma+=i
# print(suma/len(torka))

# Na programskom jeziku Python sastaviti program
# najveći i najmanji broj u torki..

# torka = (1,2,3,4,5)
# min = min(torka)
# max = max(torka)

# print(min,max)

# Na programskom jeziku Python sastaviti program
# koji spaja dve torke i sortira dobijenu torku.

torka1=(1,2,3)
torka2=(4,5,6)
nova_torka=tuple(sorted(torka1+torka2))
print(nova_torka)