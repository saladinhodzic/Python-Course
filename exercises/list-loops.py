# LISTS LOOPS

# Napisati program u programskom jeziku Python koji
# ispisuje sve parne brojeve između 1 i 20

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)
        
# i=1

# while i < 21:
#     if i % 2 == 0:
#         print(i)
#     i+=1

# Savršen broj je broj koji je jednak zbiru svih svojih delilaca
# (osim samog sebe). Na primer, broj 6 je savršen jer su
# njegovi delioci 1, 2 i 3, a zbir 1 + 2 + 3 = 6. Napisati
# program koji proverava da li je uneti broj savršen.

# broj = int(input("Unesite neki broj "))
# acc=0
# for i in range(1,broj):
#     if broj % i ==0:
#         acc+=i

# if acc == broj:
#     print("Broj je savrsen")
# else:
#     print("Broj nije savrsen")

# Napisati koji traži unos brojeva od korisnika. Kada
# korisnik unese broj 0, petlja se prekida i program
# završava.


# broj = int(input("Unesite broj "))
# while broj != 0:
#     broj = int(input("Unesite broj "))

# Napisati program koji obrće cifre unetog broja.
# Na primer, ako korisnik unese broj 1234, program
# treba da ispiše 4321.

broj = int(input("Unesite neki broj "))
novi_broj=0

while broj>0:
    ostatak = broj%10
    novi_broj=novi_broj*10 + ostatak
    broj //=10
print(novi_broj)