# TUPLES SET LIST DICTIONARY

# creating simple tuple

torka=("T","O","R","K","A")

print(torka)

# to edit tuple you firstly need to convert it to list using list() method

lista_od_torke=list(torka)

lista_od_torke.remove("R")

torka=tuple(lista_od_torke)

print(torka)

# creating simple set

skup={1,2,3,4,5}

# iterating over a set - they are unindexed

for i in skup:
    print(i)
