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

# broj = int(input("Unesite neki broj "))
# novi_broj=0

# while broj>0:
#     ostatak = broj%10
#     novi_broj=novi_broj*10 + ostatak
#     broj //=10
# print(novi_broj)

# Napisati program koji ispisuje sve proste brojeve u
# opsegu od 1 do unetog broja.

# broj = int(input("Unesite gornju granicu "))

# for i in range(2,broj):
#     prost_broj=True
#     for j in range(i-1,1,-1):
#         if i%j==0:
#             prost_broj=False
#     if prost_broj:
#         print(i)

# Napisati program koji ispisuje sve brojeve od 1 do
# 10, ali preskače broj 5..

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

# Napisati program koji proverava da li je uneti
# broj pozitivan ili negativan, ali ne reaguje kada je
# broj 0.

# broj= int(input("Unesite neki broj "))

# if broj>0:
#     print("Broj je pozitivan")
# elif broj<0:
#     print("Broj je negativan")
# else:
#     pass

# Napisati program koji ispisuje brojeve od 1 do
# 10, ali preskače sve brojeve koji su deljivi sa 3.

# for i in range(1,11):
#     if i %3==0:
#         continue
#     print(i)

# LISTS

# Napisati program u programskom jeziku Python
# koji dodaje element 'novi_element' na početak
# postojeće liste i zatim ispisuje izmenjenu listu.

# lista = [2,3,4,5]
# lista.insert(0,1)
# print(lista)

# Napisati program koji proverava da li lista
# sadrži određeni element.

# lista = [4,'ne',True, 'da']
# if lista.count('jas') > 0:
#     print("Nalazi se u listi")
# else:
#     print("Ne nalazi se u listi")

# Napisati program koji nalazi minimalnu i
# maksimalnu vrednost u listi lista = [3, 7,
# 1, 9, 4]

# lista = [3, 7, 1, 9, 4]

# # using sort method
# # lista.sort()
# # min=lista[0]
# # max=lista[-1]
# # using min and max method

# najmanji=min(lista)
# najveci = max(lista)

# # print("Najveci element u nizu je", max, 'a najmanji',min)
# print("Najveci element u nizu je", najveci, 'a najmanji',najmanji)

# Napisati program koji računa sumu svih celih
# brojeva u listi lista = [3, 'tekst', 1, 9, 4].

# lista = [3, 'tekst', 1, 9, 4]
# suma=0

# for element in lista:
#     if type(element)==int:
#         suma+=element
# # easier way is by using sum() method
# print(suma)

# Napisati program koji broji koliko je parnih i
# neparnih brojeva u listi brojevi = [1, 2, 3, 4, 5,
# 6, 7, 8, 9, 10]
# brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# parni=0
# neparni=0

# for broj in brojevi:
#     if broj % 2==0:
#         parni+=1
#     else:
#         neparni+=1
# print("Broj elemenata koji su neparni u listi su ",neparni,"a parnih je ",parni)

# Napisati program koji prolazi kroz listu brojeva lista =
# [1, 2, 3, 4, 5] i kreira novu listu gde je svakom elementu
# dodeljen njegov kvadrat. Na izlazu, ispisuje obe liste –
# originalnu i novu listu sa kvadratima brojeva.

lista = [1, 2, 3, 4, 5]
novaLista=[element*element for element in lista ]
print("Lista pre izmena ", lista, "lista posle izmena ",novaLista)

# Napisati program koji traži od korisnika da unese listu
# brojeva i zatim izdvaja brojeve veće od 4. Na izlazu
# ispisuje originalnu listu i listu brojeva većih od 4.

duzina=int(input("Unesite duzinu liste "))
i=0
lista=[]
while i<duzina:
    broj= int(input("Unesite neki broj "))
    lista.append(broj)
    i+=1

nova_lista=[element for element in lista if element > 4]

print("Originalna lista ",lista, "nova lista je ",nova_lista)