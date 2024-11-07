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

def is_armstrong_number(input):
    a=int(input[0])
    b=int(input[1])
    c=int(input[2])
    if a**3 + b**3 + c**3 == int(input):
        print("Its armstrong number")
    else:
        print("its not armstrong number")
    
is_armstrong_number(input("Unesi trocifren broj"))