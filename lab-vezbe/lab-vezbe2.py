# Korisnik unosi listu reči odvojenih razmakom, a program treba da izračuna koliko se puta
# svaka reč pojavljuje u listi, pronađe najdužu reč i izdvoji sve reči koje su palindromi. Na
# primer, za ulaznu listu ["ana", "banana", "ana", "kajak", "noc"], program ispisuje broj
# pojavljivanja reči ("ana: 2 puta", "banana: 1 puta", itd.), najdužu reč ("banana") i sve
# palindromske reči ("ana, kajak"). Ako u listi nema palindroma, ispisuje se poruka "Nema
# palindromskih reči".


lista=[]
length=int(input("Unesite duzinu niza"))

for i in range(length):
    lista.append(input("Unesite element: "))

# provera koliko se puta ispisuju date reci
check={}
for rec in lista:
    brojac=0
    for ista_rec in lista:
        if rec == ista_rec:
            brojac+=1
            check[rec]=brojac
    if rec == rec[::-1]:
        print(f"{rec} je palindrom")
print(check)