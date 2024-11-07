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

dan=input("Unesi dan")
if dan == 'nedelja' or dan == 'subota':
    print("Neradan dan")
else:
    print("radan")