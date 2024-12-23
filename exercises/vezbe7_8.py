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

def unos(n):
    niz=[]
    for _ in range(n):
        broj = int(input(f"Unesite {_+1}. broj niza "))
        niz.append(broj)
    return niz

def formiraj(prvi,drugi,n):
    novi_niz=[]
    for i in range(n):
        novi_niz.append(max(prvi[i],drugi[i]))
    return novi_niz
while True:
    n=int(input("Unesite duzinu dva niza: "))
    if n>=200 or n<=0:
        break
    
    prvi_niz=unos(n)
    drugi_niz=unos(n)
    
    novi = formiraj(prvi_niz,drugi_niz,n)
    print(novi)
