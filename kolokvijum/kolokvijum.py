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

lst = [1,2,3,1,2,4,5,6,7,8]

trenutna_najduza = []
najduza = []

for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        trenutna_najduza.append(lst[i])
    else:
        najduza = trenutna_najduza
        trenutna_najduza = []
if len(trenutna_najduza) > len(najduza):
    najduza = trenutna_najduza
print(najduza)