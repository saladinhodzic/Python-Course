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

stepen = int(input("Unesite stepen polinoma: "))
koeficijenti = [int(input("Broj: ")) for _ in range(stepen+1)]
xmin,xmax,dx = 1.0, 10.0 , 1.5
x = xmin
while x <= xmax:
    pol = 0
    for j in range(len(koeficijenti)):
        pol += koeficijenti[j]* x ** (stepen - j)
    x += dx
    print(pol)