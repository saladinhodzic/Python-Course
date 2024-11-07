# Zadaci za lab vezbe

# 1. Napisati program u kojem korisnik unosi broj godina radnog staža i ispisuje "Ispunjavaš uslov
# za napredovanje." ako je staž veći od 5 godina, u suprotnom ispisuje "Potrebno je još iskustva."

staz=int(input("Unesi godine radnog staza"))
if staz > 5:
    print("Ispunjavas uslov za napredovanje")
else:
    print("Potrebno je jos iskustva ")