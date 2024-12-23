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

niz = input("Unesite brojeve niza\n").split(" ")

niz=[int(x) for x in niz]

k= int(input("Unesite broj pozicija za rotaciju: "))

rotiran_niz= niz[k:] + niz[:k]

print(rotiran_niz)