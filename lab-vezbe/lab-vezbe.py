# Zadaci za lab vezbe

# 1. Napisati program u kojem korisnik unosi broj godina radnog staža i ispisuje "Ispunjavaš uslov
# za napredovanje." ako je staž veći od 5 godina, u suprotnom ispisuje "Potrebno je još iskustva."

# staz=int(input("Unesi godine radnog staza"))
# if staz > 5:
#     print("Ispunjavas uslov za napredovanje")
# else:
#     print("Potrebno je jos iskustva ")

# 2. Napisati program u kojem korisnik unosi email adresu i ispisuje "Validan email!" ako adresa
# sadrži karakter "@", u suprotnom ispisuje "Nevalidan email."

# email=input("unesite email adresu")
# if '@' in email:
#     print("Validan email")
# else:
#     print("Email nije validan")

# 3. Napisati program u kojem korisnik unosi lozinku i ispisuje "Lozinka je jaka!" ako je dužina
# lozinke veća od 8 karaktera, u suprotnom "Lozinka je prekratka."

# lozinka=input("Unesite lozinku")
# if len(lozinka)>8:
#     print("Lozinka je okej")
# else:
#     print("Prekratko")

# 4. Napisati program u kojem korisnik unosi dan u nedelji i ispisuje "Vikend!" ako je dan subota
# ili nedelja, u suprotnom ispisuje "Radni dan."

# dan=input("Unesi dan")
# if dan == 'nedelja' or dan == 'subota':
#     print("Neradan dan")
# else:
#     print("radan")

# 5. Napisati program u kojem korisnik unosi trocifren broj, a program treba da proveri da li je taj
# broj Armstrongov broj. Armstrongov broj (takođe poznat kao narcisistički broj) je broj čija je
# suma kubova njegovih cifara jednaka samom broju. Na primer, broj 153 je Armstrongov broj jer
# 1
# 3+53+33=153.

# def is_armstrong_number(input):
#     a=int(input[0])
#     b=int(input[1])
#     c=int(input[2])
#     if a**3 + b**3 + c**3 == int(input):
#         print("Its armstrong number")
#     else:
#         print("its not armstrong number")
    
# is_armstrong_number(input("Unesi trocifren broj"))

# 6. Napisati program u kojem korisnik unosi dva broja X i N. Program generiše sve parove celih
# brojeva (a, b) gde je a < b, a zbir a + b jednak je X. Ispisati sve takve parove.

# x=int(input("unesi prvi broj"))
# n=int(input("unesi drugi broj"))

# def is_equal_to_X(x,n):
#     for a in range(1,n):
#         for b in range(n,0,-1):
#             if a<b and a + b ==x:
#                 print(f"{a},{b}")
# is_equal_to_X(x,n)

# 7. Napisati program u kojem korisnik unosi reč i ispisuje "Duga reč" ako je dužina reči veća od 5
# karaktera, u suprotnom "Kratka reč."

# rec=input("Napisi rec")

# if len(rec)>5:
#     print("Duga rec")
# else:
#     print("Kratka rec")

# 8 Napisati program u kojem korisnik unosi broj N. Program koristi while petlju za generisanje
# brojeva od 1 do N i proverava da li su "brojevi sreće" (brojevi gde zbir kvadrata njihovih cifara
# na kraju dovodi do 1).

N=int(input("Unesi broj"))
i=1
while i<=N:
    novi=str(i)
    list=[]
    is_happy=0
    for char in novi:
        list.append(int(char))
    for num in list:
        is_happy+=num**2
    if is_happy==1:
        print(novi)
    i+=1