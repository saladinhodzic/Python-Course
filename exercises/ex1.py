# TUPLES SET LIST DICTIONARY

# creating simple tuple

torka=("T","O","R","K","A")

print(torka)

# to edit tuple you firstly need to convert it to list using list() method

lista_od_torke=list(torka)

lista_od_torke.remove("R")

torka=tuple(lista_od_torke)

print(torka)