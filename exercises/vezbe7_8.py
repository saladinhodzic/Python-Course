# NIZOVI MATRICE TORKE

# Na programskom jeziku Python sastaviti program
# koji pronalazi i ispisuje treći i posednji element
# niza

# niz = input("Unesite niz brojeva\n").split(" ")

# print(f"Treci element niza {niz[2]} a zadnji je {niz[-1]}")

# Na programskom jeziku Python sastaviti program
# koji računa zbir svih elemenata niza.

niz = input("Unesite brojeve: ").split(" ")
suma=0
for broj in niz:
    suma+=int(broj)
print(suma)