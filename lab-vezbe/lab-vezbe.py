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

# N=int(input("Unesi broj"))
# i=1
# while i<=N:
#     novi=str(i)
#     list=[]
#     is_happy=0
#     for char in novi:
#         list.append(int(char))
#     for num in list:
#         is_happy+=num**2
#     if is_happy==1:
#         print(novi)
#     i+=1

# Napisati program koji obrće cifre unetog broja.
# Na primer, ako korisnik unese broj 1234, program
# treba da ispiše 4321.

# broj=int(input("Unesite broj"))

# broj_to_string=str(broj)
# new_str=""
# for char in range(len(broj_to_string)-1,0,-1):
#     new_str+=broj_to_string[char]

# broj_reversed=int(new_str)
# print(broj_reversed)

#  Napisati program koji ispisuje sve brojeve od 1 do
# 10, ali preskače broj 5..

# for num in range(1,11):
#     if num == 5:
#         continue
#     print(num)

# Napisati program koji proverava da li je uneti
# broj pozitivan ili negativan, ali ne reaguje kada je
# broj 0.

# br=int(input("Broj"))

# if br < 0:
#     print("Broj je manji od 0")
# elif br >0:
#     print("Broj je veci od 0")
# else:
#     pass

# Napisati program u programskom jeziku Python
# koji dodaje element 'novi_element' na početak
# postojeće liste i zatim ispisuje izmenjenu listu.

# list=[1,2,3,4,5]
# list.insert(0,'da')
# print(list)

# Napisati program koji nalazi minimalnu i
# maksimalnu vrednost u listi lista = [3, 7,
# 1, 9, 4]

# lista=[3,7,1,9,4]

# najmanji=min(lista)
# najveci=max(lista)

# print(f"Najmanja vrednost liste je {najmanji} a najveca je {najveci}")

# Napisati program u programskom jeziku Python koji
# ispisuje sve parne brojeve između 1 i 20

# for i in range(1,21):
#     if i%2==0:
#         print(i)
        
# i=1

# while i<=20:
#     i+=1
    
#     if i%2==0:
#         print(i)
        
# Savršen broj je broj koji je jednak zbiru svih svojih delilaca
# (osim samog sebe). Na primer, broj 6 je savršen jer su
# njegovi delioci 1, 2 i 3, a zbir 1 + 2 + 3 = 6. Napisati
# program koji proverava da li je uneti broj savršen.

# broj=int(input("Broj "))
# delioci=0

# for i in range (1,broj):
#     if broj % i==0:
#         delioci+=i
# if delioci==broj:
#     print("savrsen ")

# Napisati koji traži unos brojeva od korisnika. Kada
# korisnik unese broj 0, petlja se prekida i program
# završava.

# broj=int(input("Unesite brojeve: ")) 

# while True:
#     broj=int(input("Unesite brojeve: ")) 
#     if broj==0:
#         break

# Napisati program koji ispisuje sve proste brojeve u
# opsegu od 1 do unetog broja.

# broj = int(input("Broj "))

# i=2
# while i<=broj:
#     prost=True
#     for b in range(2,i+1):
#         if i % b == 0:
#             prost=False
#             break
#     if prost == True:
#         print(i)
#     i+=1

# Napisati program koji ispisuje sve brojeve od 1 do
# 10, ali preskače broj 5.

# i=1

# while i<=10:
#     if i==5:
#         i+=1
        
#         continue
#     print(i)
#     i+=1
    
    
# Napisati program koji proverava da li je uneti
# broj pozitivan ili negativan, ali ne reaguje kada je
# broj 0.

# broj=int(input("Unesite broj: "))

# if broj>0:
#     print("Uneti broj je pozitivan.")
# elif broj<0:
#     print("Uneti broj je negativan.")
# else:
#     pass

# Napisati program koji ispisuje brojeve od 1 do
# 10, ali preskače sve brojeve koji su deljivi sa 3.

# i=1

# while i<=10:
#     if i%3==0:
#         pass
#     else:
#         print(i)
#     i+=1

# Napisati program koji proverava da li lista
# sadrži određeni element..


# if lista.index(3) != -1:
#     print("VERUJ MI")
# else:
#     print("NE SADRZI")
    
# if "kon" in lista:
#     print("jeste")
# else:
#     print("nije")

# Napisati program koji računa sumu svih celih
# brojeva u listi lista = [3, 'tekst', 1, 9, 4]

# lista=["konj","koza",'pasce',1,2,3]
# acc=0
# for element in lista:
#     if isinstance(element,int):
#         acc+=element
# print(acc)

# Napisati program koji broji koliko je parnih i
# neparnih brojeva u listi brojevi = [1, 2, 3, 4, 5,
# 6, 7, 8, 9, 10]

# brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# neparni=0
# parni=0

# for i in brojevi:
#     if i%2==0:
#         parni.append(i)
#     else:
#         neparni.append(i)
        

# parnilen=len(parni)
# neparnilen=len(neparni)

# print(neparnilen)
# print(parnilen)

# Napisati program koji prolazi kroz listu brojeva lista =
# [1, 2, 3, 4, 5] i kreira novu listu gde je svakom elementu
# dodeljen njegov kvadrat. Na izlazu, ispisuje obe liste –
# originalnu i novu listu sa kvadratima brojeva.

# lista = [1, 2, 3, 4, 5]
# kvadrat=[]

# for i in lista:
#     i+=pow(i,2)
#     kvadrat.append(i)
    
# print(kvadrat)
# print(lista)

# Napisati program koji traži od korisnika da unese listu
# brojeva i zatim izdvaja brojeve veće od 4. Na izlazu
# ispisuje originalnu listu i listu brojeva većih od 4.

# brojevi=input("Brojevi ")
# list=[]
# i=0
# trenutni=''
# while i<len(brojevi)-1:
#     if brojevi[i]==' ' or brojevi[i]==brojevi[-1]:
#         list.append(trenutni)
#         trenutni=''
#     else:
#         trenutni+=brojevi[i]
#     i+=1
# print(list) // neuradjen

# Napisati program u kojem korisnik unosi dva broja i proverava da li je prvi broj stepen
# drugog. Ako jeste, ispisuje "Prvi broj je stepen drugog", u suprotnom "Prvi broj nije stepen
# drugog."

# prvi_broj=int(input("Unesi prvi broj "))
# drugi_broj=int(input("Unesi drugi broj "))

# if drugi_broj ** drugi_broj == prvi_broj:
#     print("Prvi broj je stepen drugog")
# else:
#     print("Nije")

# Napisati program u kojem korisnik unosi petocifreni broj i proverava da li je broj palindrom
# (da li se čita isto sa obe strane). Ako jeste, ispisuje "Broj je palindrom", u suprotnom "Broj nije
# palindrom."

# broj = input('Uneti petocifreni broj ')

# def check_palindrom(broj):
#     novi_broj=''
#     length=len(broj)
#     for char in range(length-1,-1,-1):
#         novi_broj+=broj[char]
#     if novi_broj==broj:
#         print("Broj je palindrom")
#     else:
#         print("Broj nije palindrom")

# check_palindrom(broj)

# Napisati program u kojem korisnik unosi broj i izračunava zbir njegovih cifara, a zatim
# proverava da li je taj broj deljiv zbirom svojih cifara. Ako jeste, ispisuje "Broj je deljiv zbirom
# cifara", u suprotnom "Broj nije deljiv zbirom cifara."

# broj = input("Unesi broj ")
# zbir=0
# for br in broj:
#     zbir+=int(br)
    
# if int(broj)%zbir==0:
#     print("Broj je deljiv zbirom svojih cifara")
# else:
#     print("Nije")

# Napisati program u kojem korisnik unosi reč i proverava da li reč sadrži sve samoglasnike (a,
# e, i, o, u). Ako sadrži, ispisuje "Reč sadrži sve samoglasnike", u suprotnom "Reč ne sadrži sve
# samoglasnike."

# rec= input("Unesite rec ")

# if 'a' and 'e' and 'i' and 'o' and 'u' in rec:
#     print("Rec sadrzi sve samoglasnike")
# else:
#     print("Rec ne sadrzi sve samoglasnike")

# Za brzu orijentaciju u vezi sa stepenom gojaznosti ili mršavosti koristi se indeks telesne
# mase (engl. body mass index, skraćeno bmi). Za izračunavanje indeksa telesne mase koristi se
# formula 𝒃𝒎𝒊 =
# 𝐦
# 𝐡𝐱𝐡, gde je m masa u kilogramima, a h visina u metrima. Tumačenja vrednosti
# bmi su sledeća:

visina=float(input("Unesite vasu visinu: "))
kg=float(input("Unesite vasu masu u kilogramima: "))

formula=kg/(visina*visina)

if formula < 18.5:
    print("Premrsav si")
elif formula >=18.5 and formula <=25:
    print("Idealna razmera")
elif formula >25 and formula <=30:
    print("Vec si podebeo. Moras da smrsas.")
else:
    print("Krme debelo!")